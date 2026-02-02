from fastmcp import FastMCP
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment variables
app = FastMCP("multi-agent-mcp")

@app.tool(
    name="get_current_time",
    description="Returns the current system time"
)
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.tool(
    name="get_user_info",
    description="Greets the user by name."
)

def get_user_info(name) -> str:
    return f"Hello {name}! 👋 How can I help you today?"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, transport="http")








# from fastmcp import FastMCP
# from datetime import datetime
# from dotenv import load_dotenv
# import os

# load_dotenv()  # loads .env into environment variables

# # Optional sanity check
# if not os.getenv("OPENAI_API_KEY"):
#     raise RuntimeError("OPENAI_API_KEY not found in environment")


# app = FastMCP("Multi Agent MCP Chatbot")

# # --------------------
# # Chat Agent
# # --------------------
# def chat_agent(message: str) -> str:
#     return f"🙂 I hear you: {message}"

# app.add(
#     name="ChatAgent",
#     fn=chat_agent,       # function handling the agent logic
#     description="""
#                 You are a friendly chatbot.
#                 Respond politely to general conversation.
#                 If the user greets you or introduces themselves, respond warmly.
#                 """
# )

# # --------------------
# # Time Agent
# # --------------------
# def time_agent(message: str)-> str:
#     """
#     Return current time
#     """
#     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# app.add(
#     name="TimeAgent",
#     fn=time_agent,
#     description="""
#                 You are time assistant.
#                 Only answer questions related to time or date.
#                 """
# )


# # --------------------
# # Orchestrator Agent
# # --------------------
# def orchestrator_agent(message: str, ctx) -> str:
#     msg = message.lower()

#     if "time" in msg or "date" in msg:
#         return ctx.call_agent("TimeAgent", message)
#     else:
#         return ctx.call_agent("ChatAgent", message)
    

# app.add(
#     name="OrchestratorAgent",
#     fn=orchestrator_agent,
#     description="Route messages to ChatAgent or TimeAgent"
# )
    

# if __name__ == "__main__":
#     app.run()
