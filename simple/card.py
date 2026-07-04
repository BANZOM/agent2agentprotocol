from a2a.types import AgentCard, AgentCapabilities, AgentInterface, AgentSkill

HOST = "localhost"
PORT = 9300

 
def build_agent_card() -> AgentCard:
    return AgentCard(
        name="Greeting Agent",
        description="An agent that greets users by name.",
        version="1.0.0",
        supported_interfaces=[
            AgentInterface(url=f"http://{HOST}:{PORT}", protocol_binding="JSONRPC")
        ],
        capabilities=AgentCapabilities(streaming=False, push_notifications=False),
        skills=[
            AgentSkill(
                id="greet",
                name="Greet",
                description="Greets the user by name",
            )
        ],
    )
