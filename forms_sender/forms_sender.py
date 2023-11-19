from forms_sender.settings.config import PARAMS
from forms_sender.post_form.sender import Sender
from forms_sender.post_form.generate_form.custom_objects.profile import (
    Profile,
)

def send_forms(form_urls: list[str], profiles: list[Profile]) -> str:
    logs: str = ""
    for url in form_urls:
        for profile in profiles:
            sender = Sender(profile=profile, target_url=url)
            title: str = f"Target_url: {url}\nProfile: {profile.first_name},{profile.last_name},{profile.email}"
            log: str = sender.send_form()
            logs += f"{title}\n{log}"
    return logs