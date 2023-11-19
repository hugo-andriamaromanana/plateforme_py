import os

from forms_sender.post_form.generate_form.json_parser.json_utils import (
    load_json_from_URL,
)
from forms_sender.post_form.generate_form.custom_objects.profile import (
    Profile,
)


class Bachelor_data:
    def __init__(self, profile: Profile):
        self.path_to_preset: str = os.path.join(
            "forms_sender",
            "post_form",
            "generate_form",
            "headers_generator",
            "pages_objects",
            "init_bachelor",
            "config.json",
        )
        self.preset: dict = load_json_from_URL(self.path_to_preset)

        self.first_name: str = profile.first_name
        self.last_name: str = profile.last_name
        self.email: str = profile.email

        self.phone_number: str = self.preset["Téléphone Mobile"]
        self.title: str = self.preset["Prefixe"][0]
        self.city: str = self.preset["Ville"]
        self.postal_code: str = self.preset["Code Postal"]
        self.get_info: bool = self.preset["Obtenir simplement des renseignements"]
        self.get_entry_test: bool = self.preset[
            "Recevoir le test de sélection dès l'ouverture des inscriptions"
        ]
        self.campus: str = self.preset["Campus"][0]
        self.desired_entree_year: str = self.preset["Année d'entrée souhaitée"][0]
        self.session: str = self.preset["Session de rentrée"][0]
        self.message: str = self.preset["Message"]
        self.more_informations: bool = self.preset[
            "J'accepte de recevoir des informations de la part de La Plateforme"
        ]
        self.header: dict = {
            "Host": "laplateforme.io",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "multipart/form-data; boundary=---------------------------207529738932190165601825061531",
            "Content-Length": "8715",
            "Origin": "https://laplateforme.io",
            "Connection": "keep-alive",
            "Referer": "https://laplateforme.io/bachelor-it/init-bachelor/",
            "Cookie": "pys_start_session=true",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "iframe",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
        }
        self.payload: str = f"""
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_1.2"

{self.title}
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_1.3"

{self.first_name}
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_1.6"

{self.last_name}
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_4"

{self.email}
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_3"

{self.phone_number}
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_5.3"

{self.city}
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_5.4"


-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_5.5"

{self.postal_code}
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_5.6"

France
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_27.1"

Renseignement
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_27.2"

Candidature
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_11"

Marseille
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_25"

#01
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_28"

202402
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_17"

202409
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_22"

202402
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_19"

#01
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_20"

IT
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_32"

OUI
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_33"

NON
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_18"

Non
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_8"

{self.message}
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_6.1"

1
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_6.2"

J'accepte de recevoir des informations de la part de La Plateforme
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="input_6.3"

16
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="gform_ajax"

form_id=16&title=&description=&tabindex=0&theme=data-form-theme='orbital'
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="is_submit_16"

1
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="gform_submit"

16
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="gform_unique_id"


-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="state_16"

WyJ7XCIyNy4xXCI6XCI4OGE1YjJiMzBkNmQ1ZmYzN2FkYTcxNTMzNjYyYjU0YlwiLFwiMjcuMlwiOlwiMTA3ZDVjMWMyNWQ1YjU3M2UyNGI0ZTAzMWFiMzVhZjNcIixcIjExXCI6W1wiMTkzMjZkZjU1ODhiNDc1YWY3ZjA4ZjQ3MjFlZjEyMzlcIixcIjRlYWE3OThlODlkZWQyZmZjNWZjMjlkZjExZTgyNDQ2XCIsXCI0NGZmM2RhM2Y2MGMwY2JiOTExOGFiMjFhMjFmMzIxYlwiXSxcIjI1XCI6W1wiODBhYWM0ZjE3MDZkZGQyNTJlZTU5YjE1OGExYzU3OTFcIixcIjE5M2Y4YTg4MjNlN2IyZTViYmYyYjZlZjU0YWY3ZDVhXCIsXCIyNjI1NjZhMzAwMTYxZDQ5OWIxZWIxNDM2MjljNjdmNFwiXSxcIjI4XCI6W1wiM2MyZTI4NDc4YmUyODkyNjIzYWIxMDg4Mjk1NDcwOTFcIixcImQ5YzA2YTQ5MmM4N2E5YzNkM2ZmNjk4MWJhMGM3ODFlXCJdLFwiMzBcIjpbXCJkOWMwNmE0OTJjODdhOWMzZDNmZjY5ODFiYTBjNzgxZVwiXSxcIjEzXCI6W1wiN2I2MjQ2MjEzZDZkMjEyY2JhYjNjYzlmY2QzNzZkYWRcIixcIjY4MWQ1MTA0NTZlZjZkMGMxOWE5NDc5ZDg4M2ViZGYyXCIsXCJhZmNmNjY2MDY3NzllMzM2OGUwY2ZhNDViMDM2OTgxOVwiLFwiMmQ0ODM0ZTFhNWJmNjA1OGYyODI0N2Q0NTIzMDAxMmRcIl0sXCI2LjFcIjpcIjZhM2EzN2Y5ZDgwNWM2MDliMTA0Yzc0ZDA1MmI4Nzg1XCIsXCI2LjJcIjpcIjE0YmMwNDliN2Y2N2I4MjFkOGYzYTAxZmMwYjk1MjAxXCIsXCI2LjNcIjpcIjJmZDU3M2U2NzA2OGViMGI3ZDgwY2U4MjNjMWE3YjlkXCJ9IiwiNDgyMDBhNWYyMmI5NGYzZGRhNWRjNTMyM2YyZjRmNjYiXQ==
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="gform_target_page_number_16"

0
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="gform_source_page_number_16"

1
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="gform_field_values"


-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_hp_textarea"


-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_js"

1700410923409
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bib"

1700410975591
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bfs"

1700411240925
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bkpc"

73
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bkp"

87,59;81,44;84,352;93,23;101,101;87,70;173,465;74;77,68;131,56;62,13;119,289;73;156,43;125,20;174,214;145,75;106,95;62,484;86,84;93,90;194;107,187;76,158;80,1269;90,45;150,110;92,174;120,105;62,139;57,138;54,95;122,42;70,377;74,157;79,161;69,137;50,69;106,38;137,502;73,156;76,402;88,62;88,100;83,37;69,139;99,89;68,31;95,260;107,100;107,239;86,45;80,303;100;78;80;147;77;98,0;44,164;80,82;97,78;63,183;55,43;113,221;75,416;83,43;94,131;55,14;56,101;138,120;137,27;113,107;
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bmc"

102;71,3390;97,45528;116,6249;124,980;0,826;89,302;113,639;97,4688;106,2686;121,17432;133,1458;145,173;106,737;116,488;126,257;106,1208;108,2098;119,1798;1102,53;276,3595;111,3289;122,3463;765,8610;94,3068;68,7094;75,2442;108,579;108,834;94,3123;113,266;71,1009;0,2149;106,843;1048,-106;127,535;0,688;105,870;0,1898;258,1332;92,89;118,3264;106,1769;98,36240;103,216;97,5343;116,87670;78,5737;103,14709;102,6842;99,8696;
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bmcc"

51
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bmk"

-1;6;11;18;24;39;39;44
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bck"

1;1;1;1;38;38;38;41;49;49
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bmmc"

63
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_btmc"

0
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bsc"

0
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bte"


-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_btec"

0
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="ak_bmm"

5933,615;462,1794;1887,1820;1637,312;926,85;397,58;580,52;2807,130;2933,94;33,44;1031,270;18,280;364,283;2811,69;309,133;2273,129;4207,121;469,24;851,226;134,166;751,378;269,64;521,271;1385,170;1958,81;445,217;7870,67;1462,13;698,419;111,109;5,122;1025,82;2957,123;83,73;860,81;1728,33;1978,73;1085,98;1475,709;2312,1325;109,1355;361,1356;268,1340;2649,304;1032,136;1393,384;434,145;8,1714;231,1713;1245,1619;1666,251;40,112;2015,101;834,828;419,886;728,891;1049,87;6600,1178;581,219;663,84;2385,1961;340,870;918,142;
-----------------------------207529738932190165601825061531
Content-Disposition: form-data; name="version_hash"

1966c05b0f1cc56d18ddb486a6dd372b
-----------------------------207529738932190165601825061531--

        """
