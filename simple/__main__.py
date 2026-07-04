import uvicorn
from starlette.applications import Starlette

from a2a.server.request_handlers.default_request_handler_v2 import DefaultRequestHandlerV2
from a2a.server.routes import create_jsonrpc_routes
from a2a.server.tasks.inmemory_task_store import InMemoryTaskStore

from simple.agent_executor import GreetingAgentExecutor
from simple.card import build_agent_card, HOST, PORT


def main():
    agent_card = build_agent_card()
    handler = DefaultRequestHandlerV2(
        agent_executor=GreetingAgentExecutor(),
        task_store=InMemoryTaskStore(),
        agent_card=agent_card,
    )
    app = Starlette(routes=create_jsonrpc_routes(request_handler=handler, rpc_url="/"))

    print(f"Greeting Agent running at http://{HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
