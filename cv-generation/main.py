from dotenv import load_dotenv
from pydantic import ValidationError
from generate import generate_json_cv_using_llm
from ai_clients.openai import OpenAiClient
from ai_clients.genai import GenAiClient
from utils import store_json

load_dotenv()

if __name__ == "__main__":
    print("How many CVs would you like to generate?")
    num_cvs = int(input().strip())
    print("Which AI client would you like to use? (1) GenAI (2) OpenAI")
    client_choice = input().strip()
    if client_choice == "1":
        client = GenAiClient()
    elif client_choice == "2":
        client = OpenAiClient()
    else:
        print("Invalid choice. Using GenAI by default.")
        client = GenAiClient()
    print(f"Generating {num_cvs} CV(s)...")
    for i in range(num_cvs):
        try:
            cv_data = generate_json_cv_using_llm(client)
            filename = f"./output/generated_cv_{cv_data.email.replace('@', '_at_').replace('.', '_')}.json"
            store_json(cv_data.model_dump(), filename)
            print(f"Saved CV {i+1} to {filename}")
        except ValidationError as e:
            print(f"Validation error for CV {i+1}: {e}")
            print("Skipping this CV.")
        except Exception as e:
            print(f"An error occurred while generating CV {i+1}: {e}")
            print("Skipping this CV.")
