from generate import generate_json_cv_using_llm
from utils import store_json

if __name__ == "__main__":
    print("How many CVs would you like to generate?")
    num_cvs = int(input().strip())
    print(f"Generating {num_cvs} CV(s)...")
    for i in range(num_cvs):
        cv_data = generate_json_cv_using_llm()
        filename = f"./output/generated_cv_{i+1}.json"
        store_json(cv_data, filename)
        print(f"Saved CV {i+1} to {filename}")
        