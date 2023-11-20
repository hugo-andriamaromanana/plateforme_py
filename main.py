import forms_sender
import settings
from settings import LOGS_PATH

# ------------Current Avaiblable Urls------------------
# "https://laplateforme.io/candidatures-cursus/"
# "https://laplateforme.io/bachelor-it/init-bachelor/"

# ------------Captcha Blocked--------------------------
# "https://laplateforme.io/informations/" CAPTCHA


def main(auto_reset_config: bool = False, test_mode: bool = True):
    checker: settings.Checker = settings.Checker()
    # Making sure the json is valid
    checker.config_check()
    if checker.is_single:
        profile: forms_sender.Profile
        url: str
        profile, url = checker._generate_for_single()
        sender: dict = forms_sender.send_form(
            form_url=url, profile=profile, test_mode=test_mode
        )
    else:
        profiles: list[forms_sender.Profile]
        urls: list[str]
        profiles, urls = checker._generate_for_multiple()
        sender: dict = forms_sender.send_multiple_forms(
            form_urls=urls, profiles=profiles, test_mode=test_mode
        )
    checker.save_logs(sender)
    if auto_reset_config:
        checker.reset_config()

    print(f"[Finished] check your logs here:\n{LOGS_PATH}")


if __name__ == "__main__":
    main(auto_reset_config=False, test_mode=True)
