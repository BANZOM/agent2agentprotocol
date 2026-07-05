# Karley - Friend Agent (Google ADK)

An enthusiastic pickleball player who loves the game and is usually available.

## Stack

- **Framework**: Google ADK
- **Model**: AWS Bedrock - Amazon Nova Lite
- **Port**: 10001
- **Protocol**: A2A (JSON-RPC)

## Personality

- Upbeat and energetic
- Always excited to play pickleball
- Uses casual, friendly language with exclamation marks
- Phrases like "Oh heck yes!" or "Count me in!"

## Weekly Schedule

| Day | Availability |
|-----|-------------|
| Monday | Free after 5pm |
| Tuesday | Busy all day |
| Wednesday | Free all day |
| Thursday | Free after 3pm |
| Friday | Free all day |
| Saturday | Free morning, busy afternoon |
| Sunday | Free all day |

## Running

Started automatically by `start_agents.sh`, or manually:

```bash
export PYTHONPATH="$(pwd)"
python -m complex.karley_agent.karley
```
