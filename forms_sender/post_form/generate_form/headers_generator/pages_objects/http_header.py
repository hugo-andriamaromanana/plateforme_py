from forms_sender.post_form.generate_form.headers_generator.pages_objects.candidatures.candidatures_cursus import (
    Candidatures_data,
)
from forms_sender.post_form.generate_form.headers_generator.pages_objects.informations.informations import (
    Informations_data,
)
from forms_sender.post_form.generate_form.headers_generator.pages_objects.init_bachelor.init_bachelor import (
    Bachelor_data,
)

from forms_sender.post_form.generate_form.custom_objects.profile import (
    Profile,
)


class Http_header:
    def __init__(self, url: str, profile: Profile):
        if url not in flags:
            print(f"Exiting: {url} is not part of the program")
        flags = {
            "https://laplateforme.io/informations/": Informations_data,
            "https://laplateforme.io/candidatures-cursus/": Candidatures_data,
            "https://laplateforme.io/bachelor-it/init-bachelor/": Bachelor_data,
        }
        self.http_header = (flags[url])(profile=profile)
