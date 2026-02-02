from agents.chat_agent import ChatAgent
from agents.time_agent import TimeAgent

# It routes intent to the right agent
class OrchestratorAgent:
    def __init__(self, mcp_client):
        self.chat_agent = ChatAgent()
        self.time_agent = TimeAgent()
        self.mcp = mcp_client

    async def route(self, message: str) -> str:
        if "time" in message.lower():
            return await self.time_agent.respond(self.mcp)
        return await self.chat_agent.respond(message, self.mcp)




# from fastmcp.agent import Agent


# # It routes intent to the right agent

# orchestrator_agent = Agent(
#     name="OrchestratorAgent",
#     instructions="""
# You are an orchestratorAgent.
# Your job is to decide which agent should handle the user request.

# Routing rules:
# - If the user asks about time or date -> forward to TimeAgent
# - Otherwise -> forward to ChatAgent

# Do NOT answer directly.
# Only forward the request.
# """
# )