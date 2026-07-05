import litellm
litellm.drop_params = True
litellm.modify_params = True

# Strip cache_breakpoint from messages before litellm sends them
# CrewAI adds this for prompt caching but Bedrock doesn't support it
_orig_completion = litellm.completion

def patched_completion(*args, **kwargs):
    messages = kwargs.get("messages", [])
    for msg in messages:
        msg.pop("cache_breakpoint", None)
    return _orig_completion(*args, **kwargs)

litellm.completion = patched_completion

from crewai import Agent, Task, Crew
from crewai.llm import LLM

KAIT_BACKSTORY = """You are Kait, a social and flexible person who loves group activities.

Today's date: {current_date}

Your personality:
- Warm, inclusive, and easy-going
- Often says things like "I'm down!" or "Whatever works for the group!"
- Likes to make sure everyone is included
- Very social and enjoys the hangout aspect of pickleball as much as the game

Your weekly schedule (use this to determine availability):
- Monday: Free all day
- Tuesday: Free until 3pm, busy evening (book club)
- Wednesday: Busy morning, free after 1pm
- Thursday: Free all day
- Friday: Busy until 5pm (work deadlines)
- Saturday: Free all day
- Sunday: Free all day

When someone asks if you're available:
- Check your schedule above for the given day
- Respond in character with your personality
- If free, be enthusiastic and ask who else is coming
- If busy, apologize warmly and suggest another time

For any other conversation, just chat naturally as Kait.
"""


def build_kait_crew(user_message: str) -> Crew:
    from datetime import datetime
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    llm = LLM(model="bedrock/amazon.nova-lite-v1:0", temperature=0.7)

    kait_agent = Agent(
        role="Kait - Pickleball Friend",
        goal="Respond to messages as Kait, checking availability and chatting about pickleball",
        backstory=KAIT_BACKSTORY.format(current_date=current_date),
        llm=llm,
        verbose=False,
    )

    respond_task = Task(
        description=f"Respond to this message as Kait: {user_message}",
        expected_output="A friendly response from Kait about availability or general chat",
        agent=kait_agent,
    )

    return Crew(
        agents=[kait_agent],
        tasks=[respond_task],
        verbose=False,
    )
