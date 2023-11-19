import json


def load_json_from_URL(url: str) -> dict:
    with open(url, "r") as file:
        return json.load(file)
