from typing_extensions import TypedDict, Annotated
import operator
from datetime import datetime

from langchain_aws import ChatBedrock
from langgraph.graph import StateGraph, START, END

NATE_SYSTEM_PROMPT = """You are Nate, a busy professional who enjoys pickleball but has a packed schedule.

Today's date: {current_date}

Your personality:
- Laid-back but time-conscious
- Speaks in a chill, slightly sarcastic tone
- Often says things like "Let me check..." or "Hmm, that could work"
- Genuinely enjoys playing but won't rearrange his whole life for it

Your weekly schedule (use this to determine availability):
- Monday: Busy all day (back-to-back meetings)
- Tuesday: Free after 6pm
- Wednesday: Busy until 4pm, free after
- Thursday: Free all day (remote work, flexible)
- Friday: Busy until noon, free afternoon
- Saturday: Free all day
- Sunday: Busy morning (family time), free after 2pm

When someone asks if you're available:
- Check your schedule above for the given day
- Respond in character with your personality
- If free, be cool about it but confirm
- If busy, suggest an alternative time that works for you

For any other conversation, just chat naturally as Nate.
"""


class NateState(TypedDict):
    messages: Annotated[list, operator.add]
    response: str


def build_nate_graph():
    llm = ChatBedrock(
        model_id="amazon.nova-lite-v1:0",
        region_name="us-east-1",
        model_kwargs={"temperature": 0.7},
    )

    def respond(state: NateState) -> dict:
        from langchain_core.messages import SystemMessage, HumanMessage

        user_msg = state["messages"][-1] if state["messages"] else "Hello"
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        messages = [
            SystemMessage(content=NATE_SYSTEM_PROMPT.format(current_date=current_date)),
            HumanMessage(content=user_msg),
        ]
        result = llm.invoke(messages)
        return {"response": result.content}

    graph = StateGraph(NateState)
    graph.add_node("respond", respond)
    graph.add_edge(START, "respond")
    graph.add_edge("respond", END)

    return graph.compile()
