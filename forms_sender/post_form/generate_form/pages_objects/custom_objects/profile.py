from forms_sender.post_form.generate_form.pages_objects.custom_objects.name import (
    Generate_name,
)


class Profile:
    def __init__(
        self,
        email: str,
        auto_generate_name: bool = True,
        first_name: str = "",
        last_name: str = "",
    ):
        if auto_generate_name:
            self.first_name, self.last_name = Generate_name().generate_name()
        else:
            self.first_name, self.last_name = first_name, last_name
        self.email = email
