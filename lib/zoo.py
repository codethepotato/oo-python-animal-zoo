from lib.animal import Animal

class Zoo:
    def __init__(self, name, location):
        animals = []
        self.name = name
        self.location = location
        Zoo.animals.append(self)

    @property
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name

    @property
    def get_location(self):
        return self._location
    
    def set_location(self, new_location):
        if isinstance(new_location, str):
            self._location = new_location

    @property
    def animals(self):
        animal_list = []
        for animal in Zoo.animals: 
            if animal in Zoo.animals == self:
                animal.animals.append(self)
        return animal_list
    
    @property
    def animal_species(self):
        pass

    def find_by_species(self):
        pass

    def animal_nicknames(self):
        pass
    

