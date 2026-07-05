from a2a.types import AgentCard, AgentCapabilities, AgentInterface, AgentSkill

HOST = "localhost"
PORT = 10002


def build_agent_card() -> AgentCard:
    return AgentCard(
        name="Nate",
        description="Nate is a busy professional who enjoys pickleball but has a packed schedule. Built with LangGraph.",
        version="1.0.0",
        supported_interfaces=[
            AgentInterface(url=f"http://{HOST}:{PORT}", protocol_binding="JSONRPC")
        ],
        capabilities=AgentCapabilities(streaming=False, push_notifications=False),
        skills=[
            AgentSkill(
                id="chat",
                name="Chat",
                description="Chat with Nate about pickleball or check his availability",
            )
        ],
    )
