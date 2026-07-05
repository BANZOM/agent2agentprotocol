import asyncio

from a2a.server.agent_execution.agent_executor import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.types import Message, Part, Role

from .agent import build_kait_crew


class KaitAgentExecutor(AgentExecutor):
    def __init__(self):
        pass

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        user_text = "Hello"
        if context._params and context._params.message.parts:
            for part in context._params.message.parts:
                if part.text:
                    user_text = part.text
                    break

        # Run CrewAI in a thread to avoid event loop conflict
        crew = build_kait_crew(user_text)
        result = await asyncio.to_thread(crew.kickoff)
        response_text = str(result)

        await event_queue.enqueue_event(
            Message(
                role=Role.ROLE_AGENT,
                parts=[Part(text=response_text)],
                message_id="kait-resp",
            )
        )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        pass
