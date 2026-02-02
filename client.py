import asyncio
from fastmcp import Client
from agents.orchestrator_agent import OrchestratorAgent

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        orchestrator = OrchestratorAgent(client)

        print("🤖 Multi-Agent MCP Chatbot (type 'exit' to quit)\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break

            response = await orchestrator.route(user_input)
            print("Bot:", response)

asyncio.run(main())
