# from fastmcp.tools.tool import Tool
# from datetime import datetime

# # Define parameters expected by the tool (even if empty)
# # parameters = {}

# def get_current_time() -> str:
#     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# time_tool = Tool(
#     name="get_current_time",
#     description="Returns the current system time",
#     parameters={}  # required
# )

# def get_user_info(name) -> str:
#     return f"Hello {name}! 👋 How can I help you today?"

# greet_user_tool = Tool(
#     name="get_user_info",
#     description="Greets the user by name.",
#     parameters={}  # required
# )