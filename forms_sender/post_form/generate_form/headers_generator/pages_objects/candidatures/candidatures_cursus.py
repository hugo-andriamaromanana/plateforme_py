import os

from forms_sender.post_form.generate_form.json_parser.json_utils import (
    load_json_from_URL,
)
from forms_sender.post_form.generate_form.custom_objects.profile import (
    Profile,
)


class Candidatures_data:
    def __init__(self, profile: Profile):
        self.path_to_preset: str = os.path.join(
            "forms_sender",
            "post_form",
            "generate_form",
            "headers_generator",
            "pages_objects",
            "candidatures",
            "config.json",
        )
        self.preset: dict = load_json_from_URL(self.path_to_preset)

        self.first_name: str = profile.first_name
        self.last_name: str = profile.last_name
        self.email: str = profile.email

        self.title: str = self.preset["Prefixe"][0]
        self.city: str = self.preset["Ville"]
        self.postal_code: str = self.preset["Code Postal"]
        self.country: str = self.preset["Pays"][0]
        self.phone_number: str = self.preset["Téléphone Mobile"]
        self.get_info: bool = self.preset["Obtenir simplement des renseignements"]
        self.get_entry_test: bool = self.preset[
            "Recevoir le test de sélection dès l'ouverture des inscriptions"
        ]
        self.curriculum: str = self.preset["Cursus souhaité"]
        self.entree_year: str = self.preset["Année d'entrée souhaitée"][0]
        self.campus: str = self.preset["Campus souhaité"][0]
        self.current_diploma: str = self.preset["Niveau Actuel"][0]
        self.message: str = self.preset[
            "Quelques mots sur votre parcours et motivations"
        ]
        self.more_informations: bool = self.preset[
            "J'accepte de recevoir des informations de la part de La Plateforme"
        ]
        self.header: dict = {
            "Host": "laplateforme.io",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "multipart/form-data; boundary=---------------------------237980776240484970862145297709",
            "Content-Length": "8761",
            "Origin": "https://laplateforme.io",
            "Connection": "keep-alive",
            "Referer": "https://laplateforme.io/candidatures-cursus/",
            "Cookie": "",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "iframe",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
        }
        self.payload: str = f"""
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_1.2"

{self.title}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_1.3"

{self.first_name}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_1.6"

{self.last_name}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_4"

{self.email}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_3"

{self.phone_number}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_5.3"

{self.city}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_5.4"


-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_5.5"

{self.postal_code}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_5.6"

{self.country}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_32.1"

Renseignement
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_32.2"

Candidature
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_10"

Bachelor IT
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_15"

#{self.entree_year}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_24"

IT
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_46"

WEB2
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_50"

202403
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_49"

{self.campus}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_23"

AWS
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_22"

#01
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_14"

Marseille
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_33"

202402
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_26"

202409
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_18"

202402
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_44"

OUI
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_45"

NON
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_12"

{self.current_diploma}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_8"

{self.message}
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_6.1"

1
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_6.2"

J'accepte de recevoir des informations de la part de La Plateforme
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_6.3"

9
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="input_35"

Non
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="gform_ajax"

form_id=9&title=&description=&tabindex=0&theme=data-form-theme='orbital'
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="is_submit_9"

1
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="gform_submit"

9
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="gform_unique_id"


-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="state_9"

WyJ7XCIzMi4xXCI6XCI4OGE1YjJiMzBkNmQ1ZmYzN2FkYTcxNTMzNjYyYjU0YlwiLFwiMzIuMlwiOlwiMTA3ZDVjMWMyNWQ1YjU3M2UyNGI0ZTAzMWFiMzVhZjNcIixcIjM4XCI6W1wiMDNkYWMzM2I1YTVhMGVjODk5NjA3N2ZiMDgyZWU0NDJcIixcIjkwMjk2MmQ5MjAyZThlMjk1MzUwYWU4MzlkYmRiZDJjXCJdLFwiMzlcIjpbXCJjZTJiYmE2MjEzZDNiZWM5NGQ5Y2VlNDJmNTM4MGVhYlwiLFwiYWEyNjI5MDg0NmI5NTIxNzVmMzg0OGU4MWMzNDExYjhcIl0sXCI0MFwiOltcIjZiNjRkZWVjNGU4NmVhY2YwOGJlYzE3NmJiYjgyOGFjXCJdLFwiNDFcIjpbXCI2YjY0ZGVlYzRlODZlYWNmMDhiZWMxNzZiYmI4MjhhY1wiXSxcIjQyXCI6W1wiN2MyNzU5MDAyYWY0OTFmODQ4N2UyMDg5MmY5MDBlNjdcIl0sXCI0M1wiOltcIjQ1M2E0OWNiZGJiZTRiYWI2MTUyNTM4ZjEwMGJhYTliXCJdLFwiMzdcIjpbXCI0ZWFhNzk4ZTg5ZGVkMmZmYzVmYzI5ZGYxMWU4MjQ0NlwiLFwiMTkzMjZkZjU1ODhiNDc1YWY3ZjA4ZjQ3MjFlZjEyMzlcIl0sXCIzNlwiOltcIjRlYWE3OThlODlkZWQyZmZjNWZjMjlkZjExZTgyNDQ2XCJdLFwiMzNcIjpbXCIzYzJlMjg0NzhiZTI4OTI2MjNhYjEwODgyOTU0NzA5MVwiLFwiZDljMDZhNDkyYzg3YTljM2QzZmY2OTgxYmEwYzc4MWVcIl0sXCIzNFwiOltcImQ5YzA2YTQ5MmM4N2E5YzNkM2ZmNjk4MWJhMGM3ODFlXCJdLFwiNi4xXCI6XCI2YTNhMzdmOWQ4MDVjNjA5YjEwNGM3NGQwNTJiODc4NVwiLFwiNi4yXCI6XCIxNGJjMDQ5YjdmNjdiODIxZDhmM2EwMWZjMGI5NTIwMVwiLFwiNi4zXCI6XCI3NDVmNTMxZjQ3NTAyZWE0MWIwN2FlMjJlMDc5MWY3YlwifSIsIjBlN2IzMWEzNDI0OTFiNDNmYWZiM2RmZWNkMGU2NDczIl0=
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="gform_target_page_number_9"

0
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="gform_source_page_number_9"

1
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="gform_field_values"


-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_hp_textarea"


-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_js"

1700315802299
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bib"

1700315810947
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bfs"

1700315880584
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bkpc"

38
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bkp"

87,167;311;106,14;109,99;101,62;117,157;591;94,208;309,142;64,116;221;90,57;173;159;63,602;115,6;63,31;51,99;63,95;151;118,82;62,83;63,69;94,64;51;94,36;270,120;100,182;88,101;126,70;114,102;75,81;93,51;78;76,9;94,44;80,31;88,65;
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bmc"

99;87,4532;1,563;87,180;102,3239;95,435;84,4688;84,7325;95,463;99,2714;73,2722;90,152;93,7143;88,283;67,1066;105,224;91,275;0,1310;69,316;0,847;75,250;0,745;105,213;0,701;87,142;82,1484;1,1274;78,344;72,4260;85,281;83,455;81,1710;688,12472;63,5604;
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bmcc"

34
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bmk"

1;14;37
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bck"

4;4;18;28;28;37
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bmmc"

24
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_btmc"

0
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bsc"

7
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bte"


-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_btec"

0
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="ak_bmm"

2284,454;940,88;6,66;605,255;562,164;1635,47;1359,152;2775,113;2125,66;2163,586;600,28;1122,66;225,298;275,40;1845,120;406,428;391,69;396,66;1823,69;1074,73;3743,153;2219,167;3516,39;778,641;
-----------------------------237980776240484970862145297709
Content-Disposition: form-data; name="version_hash"

1966c05b0f1cc56d18ddb486a6dd372b
-----------------------------237980776240484970862145297709--

"""
