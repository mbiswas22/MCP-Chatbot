import os
from fastmcp import FastMCP
from datetime import datetime
from dotenv import load_dotenv
import requests


load_dotenv()  # loads .env into environment variables
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

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


@app.tool(
    name="get_weather",
    description="Get current weather for a given city"
)

def get_weather(city: str) -> str:
    if not WEATHER_API_KEY:
        return "Weather API key is missing."

    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    print(f"DEBUG response -> '{response.text}'")
    if response.status_code != 200:
        return f"Could not fetch weather for {city}"

    data = response.json()

    if data.get("cod") != 200:
        return f"City {city} not found."

    weather_desc = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return f"Current weather in {city}: {weather_desc}, Temperature: {temp}°C, Humidity: {humidity}%"


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
