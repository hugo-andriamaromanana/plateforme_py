import os

from forms_sender.json_parser.json_utils import load_json_from_URL

class Informations_data:
    def __init__(self):
        self.path_to_preset: str = os.path.join("forms_sender","pages_config","informations.json")
        self.preset: dict = load_json_from_URL(self.path_to_preset)
        self.init_form()
    
    def init_form(self):
        self.title: str = self.preset["Prefixe"][0]
        self.first_name: str = self.preset["Prénom"]
        self.last_name: str = self.preset["Nom"]
        self.email: str = self.preset["E-mail"]
        self.phone_number: str = self.preset["Téléphone Mobile"]
        self.reason: str = self.preset["Sélectionner un motif de contact"][2]
        self.message: str = self.preset["Message"]