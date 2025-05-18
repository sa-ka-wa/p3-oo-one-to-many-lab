class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all= []

    def __init__(self, name, pet_type,owner=None):
        if owner is not None:
            owner._pets.append(self)
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        self.owner = owner
        self.name = name
        self.pet_type = pet_type
        self.all.append(self)

        
    pass

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self,):
        return self._pets
    
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise ValueError("Only Pet instances can be added.")
        if pet in self._pets:
            raise ValueError("This pet is already owned by this owner.")
        if pet.owner is not None:
            raise ValueError("This pet is already owned by another owner.")
        pet.owner = self
        self._pets.append(pet)
    
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    pass
owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)
