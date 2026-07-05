from a2a.types import AgentCard, AgentCapabilities, AgentInterface, AgentSkill

HOST = "localhost"
PORT = 10001


def build_agent_card() -> AgentCard:
    return AgentCard(
        name="Karley",
        description="Karley is an enthusiastic pickleball player who loves the game and is usually available. Built with Google ADK.",
        version="1.0.0",
        supported_interfaces=[
            AgentInterface(url=f"http://{HOST}:{PORT}", protocol_binding="JSONRPC")
        ],
        capabilities=AgentCapabilities(streaming=False, push_notifications=False),
        skills=[
            AgentSkill(
                id="chat",
                name="Chat",
                description="Chat with Karley about pickleball or check her availability",
            )
        ],
    )
