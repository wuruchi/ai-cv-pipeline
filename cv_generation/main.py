import os
import logging
from dotenv import load_dotenv
from pydantic import ValidationError
from generate_cvs import generate_json_cv_using_llm
from generate_pdfs import generate_pdfs_from_available_jsons
from ai_clients.openai import OpenAiClient
from ai_clients.genai import GenAiClient
from utils import store_json

load_dotenv()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.root.setLevel(LOG_LEVEL)
logging.handlers = logging.StreamHandler()
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_multiple_cvs():
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

def export_pdfs_to_upper_directory():
    output_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "data", "cvs"))
    os.makedirs(output_dir, exist_ok=True)
    # copy generated PDFs to the new directory
    for file in os.listdir("./output"):
        if file.endswith(".pdf"):
            src = os.path.join("./output", file)
            dst = os.path.join(output_dir, file)
            os.replace(src, dst)
    print(f"Exported PDFs to {output_dir}")

if __name__ == "__main__":
    print("What would you like to do?")
    print("(1) Generate JSON CVs")
    print("(2) Generate PDF CVs from existing JSONs")
    print("(3) Export generated PDFs to ../data/cvs/")
    choice = input().strip()
    if choice == "1":
        generate_multiple_cvs()
    if choice == "2":
        generate_pdfs_from_available_jsons()
    if choice == "3":
        export_pdfs_to_upper_directory()