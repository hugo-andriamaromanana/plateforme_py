import json
import os


def load_json_from_URL(url: str) -> dict:
    with open(url, "r") as file:
        return json.load(file)


def write_to_json(content: dict, output_url: str):
    print(f"content: {content}")
    with open(output_url, "w") as file:
        json.dump(content, file, indent=4)


LOGS_PATH: str = os.path.join("logs.json")
CONFIG_PATH: str = os.path.join("settings", "config.json")

PARAMS: str = load_json_from_URL(CONFIG_PATH)

DEFAULT_PARAMS: str = {
    "single_send": {
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
