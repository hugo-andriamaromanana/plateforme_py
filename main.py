import forms_sender

# "https://laplateforme.io/candidatures-cursus/"
# "https://laplateforme.io/informations/" CAPTCHA
# "https://laplateforme.io/bachelor-it/init-bachelor/"

target = ["https://laplateforme.io/bachelor-it/init-bachelor/"]
profile1 = [forms_sender.Profile(email ="emailsqqsqqstest1@gmail.com", auto_generate_name=True)]


print(forms_sender.send_forms(target, profile1))