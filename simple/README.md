# A2A Protocol — Greeting Agent

A simple Agent-to-Agent (A2A) protocol example using the official `a2a-sdk`.

## Setup

```bash
uv sync
```

## Run the server

```bash
uv run python -m simple
```

Agent will be available at `http://localhost:9300`.

## Run the client

```bash
uv run python -m simple.client
```

## Project Structure

```
simple/
├── __main__.py        # Entrypoint — wires handler, routes, starts server
├── agent.py           # GreetingAgent — business logic
├── agent_executor.py  # A2A AgentExecutor adapter
├── card.py            # AgentCard definition
└── client.py          # Test client
```
