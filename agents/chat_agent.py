# chat_agent.py
class ChatAgent:
    async def respond(self, message: str, mcp_client) -> str:
        name = None

        lower_message = message.lower()
        if "my name is" in lower_message:
            name = lower_message.split("my name is")[-1].strip()

        if name:
            result = await mcp_client.call_tool(
                "get_user_info",
                {"name": name.capitalize()}
            )
            return result.content[0].text

        return f"Nice to meet you! 😊"






# from fastmcp import Agent

# chat_agent = Agent(
#     name="ChatAgent",
#     instructions="""You are a friendly chatbot.
#     Respond politely to general conversation.
#     If the user greets you or introduces themselves, respond warmly.
#     """
# )

# class ChatAgent:
#     async def respond(self, message: str, mcp_client) -> str:
#         # Call the tool
#         result = await mcp_client.call_tool("get_user_info", {"name": extract_name(message)})

#          # Extract the text from the CallToolResult
#         # return f"ChatAgent says: {message}"
#         return result.content[0].text
    
# def extract_name(message: str) -> str | None:
#         if "my name is" in message.lower():
#             return message.split("my name is")[-1].strip()
#         return None

    