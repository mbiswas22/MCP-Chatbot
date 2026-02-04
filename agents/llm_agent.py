# agents/llm_agent.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # loads .env into environment variables
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

class LLMAgent:
    def __init__(self):
        self.client = OpenAI(
            api_key=OPEN_AI_API_KEY
        )
        self.model = "gpt-4o-mini"  # cheaper + fast

    async def respond(self, messages: list[dict]) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message.content
