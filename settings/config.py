import json
import os


def load_json_from_URL(url: str) -> dict:
    with open(url, "r") as file:
        return json.load(file)


def write_to_json(content: dict, output_url: str):
    with open(output_url, "w") as file:
        json.dump(content, file, indent=4)


LOGS_PATH: str = os.path.join("logs.json")
LAST_LOGS: list = load_json_from_URL(LOGS_PATH)

CONFIG_PATH: str = os.path.join("settings", "config.json")

PARAMS: dict = load_json_from_URL(CONFIG_PATH)

DEFAULT_PARAMS: str = {
    "send_profile": {
        "profile": {
            "auto": False,
            "first_name": "",
            "last_name": "",
            "email": "",
        },
        "url": "",
    },
    "send_multiple_profiles": {"auto": False, "profiles": [], "urls": []},
}
