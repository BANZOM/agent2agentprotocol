from a2a.server.agent_execution.agent_executor import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.types import Message, Part, Role

from simple.agent import GreetingAgent


class GreetingAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = GreetingAgent()

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        user_text = "World"
        if context._params and context._params.message.parts:
            for part in context._params.message.parts:
                if part.text:
                    user_text = part.text
                    break

        await event_queue.enqueue_event(
            Message(
                role=Role.ROLE_AGENT,
                parts=[Part(text=self.agent.greet(user_text))],
                message_id="resp-1",
            )
        )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        pass
