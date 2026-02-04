class WeatherAgent:
    async def respond(self, message: str, mcp_client) -> str:
        city = None

        lower_message = message.lower().strip()
        
        if "weather in" in lower_message:
            city = lower_message.split("weather in")[-1].strip().title()

        if city:
            result = await mcp_client.call_tool(
                "get_weather",
                {"city": city}
            )
            return result.content[0].text

        return f"Thanks for asking! 😊"
        # Extract the text from the CallTo