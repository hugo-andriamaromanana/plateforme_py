import os

from forms_sender.post_form.generate_form.json_parser.json_utils import (
    load_json_from_URL,
)
from forms_sender.post_form.generate_form.custom_objects.profile import (
    Profile,
)


class Informations_data:
    def __init__(self, profile: Profile):
        self.path_to_preset: str = os.path.join(
            "forms_sender",
            "post_form",
            "generate_form",
            "headers_generator",
            "pages_objects",
            "informations",
            "config.json",
        )
        self.preset: dict = load_json_from_URL(self.path_to_preset)

        self.first_name: str = profile.first_name
        self.last_name: str = profile.last_name
        self.email: str = profile.email

        self.title: str = self.preset["Prefixe"][0]

        self.phone_number: str = self.preset["Téléphone Mobile"]
        self.reason: str = self.preset["Sélectionner un motif de contact"][2]
        self.message: str = self.preset["Message"]
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
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_1.2"

{self.title}
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_1.3"

{self.first_name}
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_1.6"

{self.last_name}
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_4"

{self.email}
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_3"

{self.phone_number}
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_11"

administration
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_24"

AWS
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_26"

IT
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_25"

202409
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_27"

#01
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_39"

OUI
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_40"

NON
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_42"

WEB2
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_44"

202403
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_43"

Marseille
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_8"

{self.message}
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_6.1"

1
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_6.2"

J'accepte de recevoir des informations de la part de La Plateforme
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_6.3"

11
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="input_32"

Non
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="gform_ajax"

form_id=11&title=&description=&tabindex=0&theme=data-form-theme='orbital'
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="is_submit_11"

1
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="gform_submit"

11
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="gform_unique_id"

655a3e4837337
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="state_11"

WyJ7XCIzMC4xXCI6XCI4OGE1YjJiMzBkNmQ1ZmYzN2FkYTcxNTMzNjYyYjU0YlwiLFwiMzAuMlwiOlwiMTA3ZDVjMWMyNWQ1YjU3M2UyNGI0ZTAzMWFiMzVhZjNcIixcIjMxXCI6W1wiNDUzYTQ5Y2JkYmJlNGJhYjYxNTI1MzhmMTAwYmFhOWJcIixcImQ5YzA2YTQ5MmM4N2E5YzNkM2ZmNjk4MWJhMGM3ODFlXCJdLFwiMjhcIjpbXCI0ZWFhNzk4ZTg5ZGVkMmZmYzVmYzI5ZGYxMWU4MjQ0NlwiXSxcIjE0LjFcIjpcImFmYTEzYjUyMGI2NTljNjU0NmRkMzg3Y2Y5ZTM4NTliXCIsXCIxNC4yXCI6XCJhZWM2ODA0YzhkOTM3NDdkYTBlMjA0NmE1OTYwMjRmYlwiLFwiMTQuM1wiOlwiZGM5MjMwMDNlYWUzOWYwMDQ0ZGY1OGU0YTdiYWUzZjFcIixcIjE0LjRcIjpcIjQ1Y2YwMzYzZDQ0NzVkYjYxYzI0MGYxYzFkMjlhNzNhXCIsXCIxNlwiOltcIjEzMjBjN2UyOWYxOWJkZDIxYTA0ZTI5NTIyZmQ1NTRhXCIsXCJkNDdkNWZkMmQ1YjkzZGY0YWNjMzMzMDc1MzA2MDQxZVwiLFwiOGNkMjIwNmNkODMzYjNlZDkwNTkyNDhlNWQ2NmRjZThcIixcIjFiZGRjYTY3NjU5YjM3ZDBjM2NkOGY0NjlmNDY5MmVjXCIsXCIzOWJkZjhmYzI3ZWNjZTYzNTBlMTE4MmNlZTMwOGNjZFwiLFwiNDVjZjAzNjNkNDQ3NWRiNjFjMjQwZjFjMWQyOWE3M2FcIl0sXCI2LjFcIjpcIjZhM2EzN2Y5ZDgwNWM2MDliMTA0Yzc0ZDA1MmI4Nzg1XCIsXCI2LjJcIjpcIjE0YmMwNDliN2Y2N2I4MjFkOGYzYTAxZmMwYjk1MjAxXCIsXCI2LjNcIjpcIjVmMDRhYTNiNGZmYTg2YWE0NjIzNDkxYTBlMWZhMzgwXCJ9IiwiN2RmOTczMjllNjQ0MTA2NzgyNWM5NjZiYzMzZWJmNzQiXQ==
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="gform_target_page_number_11"

0
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="gform_source_page_number_11"

1
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="gform_field_values"


-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="ak_hp_textarea"


-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="ak_js"

1700413000294
-----------------------------1706806541189042364160004875
Content-Disposition: form-data; name="version_hash"

1966c05b0f1cc56d18ddb486a6dd372b
-----------------------------1706806541189042364160004875--

"""
