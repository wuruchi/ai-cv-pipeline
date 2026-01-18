import os
from perplexity import Perplexity
from ai_clients.client import AiClient

API_KEY = os.getenv("PERPLEXITY_API_KEY")

class PerplexityAiClient(AiClient):
    def __init__(self, model: str = "sonar-pro"):
        super().__init__(model)
        self.client = Perplexity(api_key=API_KEY)

    def query(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content