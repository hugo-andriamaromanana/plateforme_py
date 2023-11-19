from forms_sender.post_form.generate_form.headers_generator.pages_objects.http_header import (
    Http_header,
)

from forms_sender.post_form.generate_form.custom_objects.profile import (
    Profile,
)

class Header:
    def __init__(self, url: str, profile: Profile):
        header: Http_header = Http_header(url=url, profile= profile)
        self.header: str = header.http_header.header
        self.payload: str = header.http_header.payload
