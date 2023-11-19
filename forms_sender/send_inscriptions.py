from forms_sender.settings.config import PARAMS
from forms_sender.post_form.sender import Sender
from forms_sender.post_form.generate_form.custom_objects.profile import (
    Profile,
)

candidature_url = "https://laplateforme.io/candidatures-cursus/"
profile = Profile(
    email="thekillerharold@gmail.com", first_name="test", last_name="test"
)

sender = Sender(profile=profile, target_url=candidature_url)

print(sender.send_form())
