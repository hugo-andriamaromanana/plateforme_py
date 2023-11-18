import requests
from forms_sender.pages_objects.candidatures_cursus_object import Candidatures_data

class Sender:
    def __i
    def send_to_candidatures(self, email: str, first_name: str = "", last_name: str = ""):
        session = Candidatures_data(email, first_name, last_name)
        