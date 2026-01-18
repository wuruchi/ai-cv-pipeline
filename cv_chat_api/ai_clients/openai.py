import os
from ai_clients.client import AiClient
from openai import OpenAI

MODEL_ID = "openai/gpt-4o-mini"

class OpenAiClient(AiClient):
    def __init__(self, model: str = MODEL_ID):
        super().__init__(model)
        API_KEY = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=API_KEY, base_url="https://openrouter.ai/api/v1")

    def query(self, prompt):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
        )
        return completion.choices[0].message.content
    