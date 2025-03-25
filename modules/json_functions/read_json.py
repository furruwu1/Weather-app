import json
import os

def read_json(file_name: str):
    static_path = os.path.abspath(__file__ + f"../../../../static/{file_name}")
    with open(static_path, "r") as file:
        return json.load(file)
