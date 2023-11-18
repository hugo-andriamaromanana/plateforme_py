import os

from forms_sender.json_parser.json_utils import load_json_from_URL


class Bachelor_data:
    def __init__(self):
        self.path_to_preset: str = os.path.join(
            "forms_sender", "pages_config", "init_bachelor.json"
        )
        self.preset: dict = load_json_from_URL(self.path_to_preset)
        self.init_form()
        
    def init_form(self):
        self.title: str = self.preset["Prefixe"][0]
        self.first_name: str = self.preset["Prénom"]
        self.last_name: str = self.preset["Nom"]
        self.email: str = self.preset["E-mail"]
        self.city: str = self.preset["Ville"]
        self.postal_code: str = self.preset["Code Postal"]
        self.get_info: bool = self.preset["Obtenir simplement des renseignements"]
        self.get_entry_test: bool = self.preset[
            "Recevoir le test de sélection dès l'ouverture des inscriptions"
        ]
        self.campus: str = self.preset["Campus souhaité"][0]
        self.desired_entree_year: str = self.preset["Année d'entrée souhaitée"][0]
        self.message: str = self.preset["Message"]
        self.more_informations: bool = self.preset[
            "J'accepte de recevoir des informations de la part de La Plateforme"
        ]