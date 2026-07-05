import litellm
litellm.drop_params = True
litellm.modify_params = True

from google.adk.agents import Agent

from .tools import send_message, book_pickleball_court, list_court_available, get_current_date

root_agent = Agent(
    name="banzo_agent",
    model="bedrock/amazon.nova-lite-v1:0",
    description="Banzo is a host agent that coordinates pickleball games with friends.",
    instruction=(
        "You are Banzo, a friendly agent who helps organize pickleball games. "
        "You have the following friend agents:\n"
        "- karley: Enthusiastic pickleball player, usually available. Built with Google ADK.\n"
        "- nate: Busy professional who enjoys pickleball but has a packed schedule. Built with LangGraph.\n"
        "- kait: Social and flexible person who loves group activities. Built with CrewAI.\n\n"
        "- Use get_current_date to check today's date before asking about availability.\n"
        "- Use send_message to chat with a specific friend (karley, nate, or kait).\n"
        "- Use list_court_available to check which friends are free on a date.\n"
        "- Use book_pickleball_court to book a court once you've confirmed availability.\n"
        "Always check the current date first, then check friends' availability before booking a court."
    ),
    tools=[get_current_date, send_message, book_pickleball_court, list_court_available],
)
