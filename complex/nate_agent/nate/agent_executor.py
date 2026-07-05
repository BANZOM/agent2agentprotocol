from a2a.server.agent_execution.agent_executor import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.types import Message, Part, Role

from .agent import build_nate_graph


class NateAgentExecutor(AgentExecutor):
    def __init__(self):
        self.graph = build_nate_graph()

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        user_text = "Hello"
        if context._params and context._params.message.parts:
            for part in context._params.message.parts:
                if part.text:
                    user_text = part.text
                    break

        result = await self.graph.ainvoke({"messages": [user_text], "response": ""})
        response_text = result.get("response", "Hey, something went wrong on my end.")

        await event_queue.enqueue_event(
            Message(
                role=Role.ROLE_AGENT,
                parts=[Part(text=response_text)],
                message_id="nate-resp",
            )
        )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        pass
