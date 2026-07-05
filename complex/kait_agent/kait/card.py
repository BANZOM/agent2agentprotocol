from a2a.types import AgentCard, AgentCapabilities, AgentInterface, AgentSkill

HOST = "localhost"
PORT = 10003


def build_agent_card() -> AgentCard:
    return AgentCard(
        name="Kait",
        description="Kait is a social and flexible person who loves group activities and pickleball. Built with CrewAI.",
        version="1.0.0",
        supported_interfaces=[
            AgentInterface(url=f"http://{HOST}:{PORT}", protocol_binding="JSONRPC")
        ],
        capabilities=AgentCapabilities(streaming=False, push_notifications=False),
        skills=[
            AgentSkill(
                id="chat",
                name="Chat",
                description="Chat with Kait about pickleball or check her availability",
            )
        ],
    )
