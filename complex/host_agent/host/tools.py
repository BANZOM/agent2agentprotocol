import asyncio
from datetime import datetime

from .host_agent import HostAgent

REMOTE_AGENT_ADDRESSES: dict[str, str] = {
    "karley": "http://localhost:10001",
    "nate": "http://localhost:10002",
    "kait": "http://localhost:10003",
}

_host_agent: HostAgent | None = None
_initialized: bool = False


async def _get_host_agent() -> HostAgent:
    """Lazily initialize the HostAgent on first use."""
    global _host_agent, _initialized
    if not _initialized:
        _host_agent = HostAgent(REMOTE_AGENT_ADDRESSES)
        await _host_agent.async_init_components()
        _initialized = True
    return _host_agent


async def get_current_date() -> str:
    """Get the current date and day of the week."""
    now = datetime.now()
    return now.strftime("%A, %B %d, %Y (%-I:%M %p)")


async def send_message(agent_name: str, message: str) -> str:
    """Send a message to a friend agent (karley, nate, or kait) to chat or ask questions."""
    host = await _get_host_agent()
    return await host.send_message_to(agent_name, message)


async def list_court_available(date: str) -> str:
    """Check which friends are available for pickleball on a given date by asking all of them."""
    host = await _get_host_agent()
    results = []
    for name in host.agents:
        response = await host.send_message_to(name, f"Are you available to play pickleball on {date}?")
        results.append(f"{name}: {response}")
    return "\n".join(results)


async def book_pickleball_court(court_name: str, date: str, time: str) -> str:
    """Book a pickleball court once availability is confirmed with friends."""
    return f"Booked court '{court_name}' on {date} at {time}. Have fun!"
