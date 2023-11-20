import forms_sender
import settings
from settings import LOGS_PATH

#------------Current Avaiblable Urls------------------
# "https://laplateforme.io/candidatures-cursus/"
# "https://laplateforme.io/bachelor-it/init-bachelor/"
#------------Captcha Blocked--------------------------
# "https://laplateforme.io/informations/" CAPTCHA

def main():
    checker: settings.Checker = settings.Checker()
    #Making sure the json is valid
    checker.config_check()
    print(checker.is_single)
    if checker.is_single:
        checker.generate_for_single()
        sender: dict = forms_sender.send_form(checker.url, checker.profile)
    else:
        checker.generate_for_multiple()
        sender: dict = forms_sender.send_multiple_forms(checker.url, checker.profile)
    checker.save_logs(sender)
    # checker.reset_config()
    print(f"[reset] config reset")
    print(f"[Finished] check your logs here\n{LOGS_PATH}")
    
if __name__ == "__main__":
    main()