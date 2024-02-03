from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def create_new_pet(self, pet_type):
        pass

    def create_pet(self, pet_type, name, date):
        pet = self.create_new_pet(pet_type)
        pet.set_name(name)
        pet.set_birthday(date)
        return pet
