from Model.pets import PetCreator
from Counter.counter import Counter


class PetRegistry:
    def __init__(self):
        self.pet_creator = PetCreator()
        self.registry = {}

    def add_pet(self, pet_type, name, birthday):
        pet = self.pet_creator.create_pet(pet_type, name, birthday)
        pet_id = len(self.registry) + 1
        pet.set_pet_id(pet_id)
        self.registry[pet_id] = pet

    def determine_pet_class(self, pet_id):
        if pet_id in self.registry:
            pet = self.registry[pet_id]
            return pet.__class__.__name__
        else:
            return "Животное не найдено"

    def show_pet_commands(self, pet_id):
        if pet_id in self.registry:
            pet = self.registry[pet_id]
            return f"{pet.__class__.__name__} поддерживает следующие команды: {pet.commands()}"
        else:
            return "Животное не найдено"

    def teach_pet_command(self, pet_id, command):
        if pet_id in self.registry:
            pet = self.registry[pet_id]
            pet.teach(command)
            return f"Команда '{command}' добавлена для {pet.__class__.__name__}"
        else:
            return "Животное не найдено"
