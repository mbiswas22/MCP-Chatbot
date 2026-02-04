# # agents/llm_agent.py
# import httpx

# class LLMAgent:
#     def __init__(self):
#         self.endpoint = "http://localhost:11434/v1/chat/completions"
#         self.model = "llama3"

#     async def respond(self, messages):
#         payload = {
#             "model": self.model,
#             "messages": messages,
#             "temperature": 0.7
#         }

#         async with httpx.AsyncClient() as client:
#             response = await client.post(self.endpoint, json=payload)
#             data = response.json()

#         return data["choices"][0]["message"]["content"]
