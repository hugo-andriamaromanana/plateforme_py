from faker import Faker


class Generate_name:
    def __init__(self):
        self.fake = Faker()

    def generate_name(self):
        name = self.fake.name()
        name_array = name.split(" ")
        first_name, last_name = name_array[0], name_array[1]
        return first_name, last_name
