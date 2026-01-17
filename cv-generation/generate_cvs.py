import json
from ai_clients.client import AiClient
from prompt import CV_GENERATION_PROMPT
from data_structures import CV

def generate_json_cv_using_llm(client: AiClient) -> CV:
    prompt = CV_GENERATION_PROMPT
    response = client.create(prompt)
    cv_data = json.loads(response)
    return CV(**cv_data)
