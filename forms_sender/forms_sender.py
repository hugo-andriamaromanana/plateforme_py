from forms_sender.settings.config import PARAMS
from forms_sender.post_form.sender import Sender
from forms_sender.post_form.generate_form.custom_objects.profile import (
    Profile,
)
import time
from datetime import datetime, date


def send_form(form_url: str, profile: Profile) -> dict:
    """
    Send a inscription form with the corresponding profile to the specified
    url if it's in the db and returns the reponse log as a dictionnary

    Args:
        form_url: the target url where the form will be sent
        profile: constitute a name, last name, email and will be the
        "profile" sent

    Returns:
        A dictionnary that sums up how the request went, if and how it
        got there
    """
    sender = Sender(profile=profile, target_url=form_url)
    sender.send_form()
    current_date = date.today()
    current_time = (datetime.now()).strftime("%H:%M:%S")
    return {
        "date": current_date,
        "time": current_time,
        "first_name": profile.first_name,
        "last_name": profile.last_name,
        "email": profile.email,
        "sucess": sender.success,
        "log": sender.text_output,
    }


def send_multiple_forms(form_urls: list[str], profiles: list[Profile]) -> list[dict]:
    """
    Send Inscriptions forms which each profiles to ALL specified urls
    so 3 profiles and 3 urls will result in 9 requests

    Args:
        form_urls: the array of targeted urls
        profiles: name, last name, email that will be sent with the forms

    Return:
        An array of dictionnaries of all the requests' log

    Example:
        send_multiple_forms(array_of_url, array_of_all_profiles)
        >>> [
            {
        "date": current date,
        "time": current time,
        "first_name": first name,
        "last_name": last name,
        "email": email,
        "sucess": success,
        "log": text_output,},{...}]
    """
    logs: list = []
    for url in form_urls:
        for profile in profiles:
            logs.append(send_form(url, profile))
            time.sleep(5)
    return logs
