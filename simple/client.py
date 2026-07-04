import asyncio

import httpx

from a2a.client.card_resolver import A2ACardResolver
from a2a.client.client_factory import ClientFactory
from a2a.types import Message, Part, Role, SendMessageRequest

from simple.card import HOST, PORT

BASE_URL = f"http://{HOST}:{PORT}"


async def main():
    async with httpx.AsyncClient() as http_client:
        # Resolve agent card
        resolver = A2ACardResolver(httpx_client=http_client, base_url=BASE_URL)
        card = await resolver.get_agent_card()
        print(f"Discovered agent: {card.name}")

        # Create A2A client from card
        client = ClientFactory().create(card)

        # Send message
        request = SendMessageRequest(
            message=Message(
                message_id="msg-1",
                role=Role.ROLE_USER,
                parts=[Part(text="Aditya")],
            )
        )
        async for response in client.send_message(request):
            print(response)

        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
