
class TimeAgent:
    async def respond(self, mcp_client) -> str:
        # Call the tool
        result = await mcp_client.call_tool("get_current_time")
        
        # Extract the text from the CallToolResult
        return result.content[0].text
    




    

# from fastmcp import Agent
# from tools import get_current_time

# time_agent = Agent(
#     name="TimeAgent",
#     instructions="""
# You are time assistant.
# Only answer questions related to time or date.
# Always use the get _current_time tool.
# """,
# tools=[get_current_time]
# )