import requests

from forms_sender.settings.config import PARAMS
from forms_sender.post_form.generate_form.custom_objects.profile import (
    Profile,
)

from forms_sender.post_form.generate_form.headers_generator.headers import Header


class Sender:
    def __init__(self, profile: Profile, target_url: str):
        self.target_url: str = target_url
        self.headers = Header(url=self.target_url, profile= profile)

    def send_form(self):
        session: requests.Session = requests.Session()
        try:
            response: requests.Response = session.post(
                self.target_url, headers=self.headers.header, data=self.headers.payload
            )
            print(f"[Sucess] POST made")
        except:
            return f"[Fail] could not POST"
        self.success: bool = response.status_code == 200
        self.text_output: str = response.text
        result = "[Sucess]" if self.success else "[Fail]"
        return f"\n{result}\nResponse:{self.text_output}"
