import json
import os

def write_json(file_name: str, file_value):
    static_path = os.path.abspath(__file__+f"../../../../static/{file_name}")
    #print("file_value", file_value)
    with open(file=static_path, mode="w") as file:
        json.dump(
            obj=file_value,
            fp=file,
            indent=4
        )