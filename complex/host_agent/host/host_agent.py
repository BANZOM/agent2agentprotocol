import uuid

import httpx

from a2a.client.card_resolver import A2ACardResolver
from a2a.client.client_factory import ClientFactory
from a2a.client.client import Client
from a2a.types import AgentCard, Message, Part, Role, SendMessageRequest


class HostAgent:
    def __init__(self, remote_agent_addresses: dict[str, str]) -> None:
        """Initialize the host agent with remote agent URLs.

        Args:
            remote_agent_addresses: Mapping of agent name to base URL.
                e.g. {"karley": "http://localhost:1001", ...}
        """
        self.agents: dict[str, dict[str, str | AgentCard | Client]] = {
            name: {"url": url} for name, url in remote_agent_addresses.items()
        }

    async def async_init_components(self) -> None:
        """Resolve agent cards and create clients for all remote agents."""
        async with httpx.AsyncClient() as http_client:
            for name, info in self.agents.items():
                resolver = A2ACardResolver(httpx_client=http_client, base_url=info["url"])
                card = await resolver.get_agent_card()
                info["card"] = card
                info["client"] = ClientFactory().create(card)

    async def send_message_to(self, agent_name: str, text: str) -> str:
        """Send a task to a specific remote agent and return the response."""
        client: Client = self.agents[agent_name]["client"]
        request = SendMessageRequest(
            message=Message(
                message_id=str(uuid.uuid4()),
                role=Role.ROLE_USER,
                parts=[Part(text=text)],
            )
        )

        result = ""
        async for response in client.send_message(request):
            if response.task and response.task.artifacts:
                for artifact in response.task.artifacts:
                    for part in artifact.parts:
                        if part.text:
                            result += part.text
            elif response.message and response.message.parts:
                for part in response.message.parts:
                    if part.text:
                        result += part.text
        return result

    async def close(self) -> None:
        """Close all remote agent clients."""
        for info in self.agents.values():
            if "client" in info:
                await info["client"].close()
