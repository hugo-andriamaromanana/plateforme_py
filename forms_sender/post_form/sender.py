import requests

from forms_sender.post_form.generate_form.pages_objects.candidatures_cursus import Candidatures_data
from forms_sender.post_form.generate_form.pages_objects.custom_objects.profile import Profile

from forms_sender.settings.config import PARAMS


class Sender:
    def __init__(self, profile: Profile, target_url: str):
        self.target_url: str = target_url
        self.profile: Profile = profile

    def sender(self):
        flags = {
            "https://laplateforme.io/informations/": self.send_to_informations,
            "https://laplateforme.io/candidatures-cursus/": self.send_to_candidatures,
            "https://laplateforme.io/bachelor-it/init-bachelor/": self.send_to_init_bachelor,
        }
        self.response: requests.Response = flags[self.target_url]()
        print(self.response.text)
        self.success: bool = self.response.status_code == 200
        self.log: str = self.response.text

    def send_to_candidatures(self):
        http_headers: Candidatures_data = Candidatures_data(self.profile)
        session: requests.Session = requests.Session()
        response: requests.Response = session.post(
            self.target_url, headers=http_headers.header, data=http_headers.payload
        )
        print("[Done] Request sent")
        return response
        
    def send_to_informations(self):
        pass

    def send_to_init_bachelor(self):
        pass