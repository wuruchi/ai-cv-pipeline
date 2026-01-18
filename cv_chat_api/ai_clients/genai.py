import os
from google import genai
from ai_clients.client import AiClient

MODEL_ID = "gemini-2.5-flash"

class GenAiClient(AiClient):
    def __init__(self, model: str = MODEL_ID):
        super().__init__(model)
        API_KEY = os.getenv("GENAI_API_KEY")
        self.client = genai.Client(api_key=API_KEY)

    def query(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            },
        )    
        return response.text
