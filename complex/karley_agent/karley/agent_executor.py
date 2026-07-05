from a2a.server.agent_execution.agent_executor import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.types import Message, Part, Role

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part as GenAIPart

from .agent import build_karley_agent


class KarleyAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = build_karley_agent()
        self.session_service = InMemorySessionService()
        self.runner = Runner(
            agent=self.agent,
            app_name="karley_app",
            session_service=self.session_service,
        )

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        user_text = "Hello"
        if context._params and context._params.message.parts:
            for part in context._params.message.parts:
                if part.text:
                    user_text = part.text
                    break

        # Create or reuse a session
        session = await self.session_service.create_session(
            app_name="karley_app", user_id="host_agent"
        )

        user_content = Content(
            role="user", parts=[GenAIPart(text=user_text)]
        )

        response_text = ""
        async for event in self.runner.run_async(
            session_id=session.id, user_id="host_agent", new_message=user_content
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        response_text += part.text

        await event_queue.enqueue_event(
            Message(
                role=Role.ROLE_AGENT,
                parts=[Part(text=response_text)],
                message_id="karley-resp",
            )
        )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        pass
