from forms_sender.post_form.generate_form.headers_generator.pages_objects.http_header import (
    Http_header,
)


class Header:
    def __init__(self, url: str):
        header: Http_header = Http_header(url=url)
        self.header: str = header.http_header.header
        self.payload: str = header.http_header.payload
