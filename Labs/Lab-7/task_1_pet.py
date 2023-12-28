class Pet:
    def __init__(self, name, age, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    
    # Set functions are useless in this case, but I'm including them for the sake of completeness
    def set_name(self, name):
        self.name = name
    
    def set_animal_type(self, animal_type):
        self.animal_type = animal_type
        
    def set_age(self, age):
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_animal_type(self):
        return self.animal_type 
    
    def get_age(self):
        return self.age