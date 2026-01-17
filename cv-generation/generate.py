import os
import json
from google import genai
from dotenv import load_dotenv
from prompt import CV_GENERATION_PROMPT

load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

MODEL_ID = "gemini-2.5-flash"

client = genai.Client(api_key=API_KEY)

def generate_json_cv_using_llm() -> dict:
    prompt = CV_GENERATION_PROMPT
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        },
    )    
    cv_data = json.loads(response.text)
    return cv_data

