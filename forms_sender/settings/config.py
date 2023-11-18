import json
import os

def load_json_from_URL(url: str) -> dict:
    with open(url, "r") as file:
        return json.load(file)

PARAMS = load_json_from_URL(os.path.join("forms_sender","settings","config.json"))
