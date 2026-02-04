from agents.chat_agent import ChatAgent
from agents.time_agent import TimeAgent
from agents.weather_agent import WeatherAgent
from agents.llm_agent import LLMAgent

# It routes intent to the right agent
class OrchestratorAgent:
    def __init__(self, mcp_client):
        self.chat_agent = ChatAgent()
        self.time_agent = TimeAgent()
        self.weather_agent = WeatherAgent()
        self.llm_agent = LLMAgent()
        self.mcp = mcp_client

        # conversation memory (FREE)
        self.memory = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    async def route(self, message: str) -> str:
        # save user message
        self.memory.append({"role": "user", "content": message})

         # 1️⃣ Try tool-based response
        chat_response = await self.chat_agent.respond(message, self.mcp)

        if "time" in message.lower():
            tool_time_res = await self.time_agent.respond(self.mcp)
            self.memory.append({"role": "assistant", "content": tool_time_res})
            return tool_time_res
        elif "weather" in message.lower():
            tool_weather_res = await self.weather_agent.respond(message, self.mcp)
            self.memory.append({"role": "assistant", "content": tool_weather_res})
            return tool_weather_res
        elif chat_response:
            self.memory.append({"role": "assistant", "content": chat_response})
            return chat_response
        
 # 2️⃣ Fallback to OpenAI
        llm_response = await self.llm_agent.respond(self.memory)
        self.memory.append({"role": "assistant", "content": llm_response})

        return llm_response



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