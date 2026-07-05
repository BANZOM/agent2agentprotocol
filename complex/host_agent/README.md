# Banzo - Host Agent (Google ADK)

The orchestrator agent that coordinates pickleball games by communicating with friend agents via A2A protocol.

## Stack

- **Framework**: Google ADK
- **Model**: AWS Bedrock - Amazon Nova Lite
- **Role**: Host / Orchestrator

## Tools

| Tool | Description |
|------|-------------|
| `get_current_date` | Get today's date and time |
| `send_message` | Chat with a specific friend agent |
| `list_court_available` | Ask all friends about availability on a date |
| `book_pickleball_court` | Book a court after confirming availability |

## How It Works

1. User sends a message via `adk web` UI
2. Banzo uses tools to communicate with remote agents (Karley, Nate, Kait) over A2A
3. Remote agents respond with availability info
4. Banzo books a court and confirms with everyone

## Running

```bash
./complex/start_host.sh
```

Requires remote agents to be running first (`start_agents.sh`).
