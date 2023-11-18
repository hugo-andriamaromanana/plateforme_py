from faker import Faker

class Generate_names:
    def __init__(self, nb_of_names):
        self.fake = Faker()
        self.nb_of_names = nb_of_names
    
    def generate_names(self):
        names_array = [] 
        for _ in range(self.nb_of_names):
            names_array.append(self.fake.name())
        return names_array
    
    