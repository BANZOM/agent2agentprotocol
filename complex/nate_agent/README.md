# Nate - Friend Agent (LangGraph)

A busy professional who enjoys pickleball but has a packed schedule.

## Stack

- **Framework**: LangGraph (LangChain)
- **Model**: AWS Bedrock - Amazon Nova Lite (via ChatBedrock)
- **Port**: 10002
- **Protocol**: A2A (JSON-RPC)

## Personality

- Laid-back but time-conscious
- Chill, slightly sarcastic tone
- Phrases like "Let me check..." or "Hmm, that could work"
- Enjoys playing but won't rearrange his whole life for it

## Weekly Schedule

| Day | Availability |
|-----|-------------|
| Monday | Busy all day |
| Tuesday | Free after 6pm |
| Wednesday | Free after 4pm |
| Thursday | Free all day |
| Friday | Free afternoon |
| Saturday | Free all day |
| Sunday | Free after 2pm |

## Architecture

Uses a simple LangGraph `StateGraph` with a single `respond` node:

```
START -> respond -> END
```

The `respond` node takes the user message, prepends a system prompt with personality and schedule, and returns the LLM response.

## Running

Started automatically by `start_agents.sh`, or manually:

```bash
export PYTHONPATH="$(pwd)"
python -m complex.nate_agent.nate
```
