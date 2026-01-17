import json 

def store_json(data: dict, filename: str):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
        