import json

import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from a2a.server.request_handlers.default_request_handler_v2 import DefaultRequestHandlerV2
from a2a.server.routes import create_jsonrpc_routes
from a2a.server.tasks.inmemory_task_store import InMemoryTaskStore
from google.protobuf.json_format import MessageToDict

from simple.agent_executor import GreetingAgentExecutor
from simple.card import build_agent_card, HOST, PORT


def main():
    agent_card = build_agent_card()
    handler = DefaultRequestHandlerV2(
        agent_executor=GreetingAgentExecutor(),
        task_store=InMemoryTaskStore(),
        agent_card=agent_card,
    )

    async def agent_card_endpoint(request: Request):
        return JSONResponse(MessageToDict(agent_card))

    routes = [
        Route("/.well-known/agent-card.json", agent_card_endpoint, methods=["GET"]),
        *create_jsonrpc_routes(request_handler=handler, rpc_url="/"),
    ]
    app = Starlette(routes=routes)

    print(f"Greeting Agent running at http://{HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
