from Model.pet import Pet
from Model.creator import Creator
from abc import ABC, abstractmethod
from datetime import datetime

class Cat(Pet):
    def __str__(self):
        return f"{self.get_pet_id()}. {self.__class__.__name__}: имя: {self.get_name()}, дата рождения: {self.get_birthday()}"

class Dog(Pet):
    def __str__(self):
        return f"{self.get_pet_id()}. {self.__class__.__name__}: имя: {self.get_name()}, дата рождения: {self.get_birthday()}"

class Hamster(Pet):
    def __str__(self):
        return f"{self.get_pet_id()}. {self.__class__.__name__}: имя: {self.get_name()}, дата рождения: {self.get_birthday()}"

class PetType:
    Cat = 1
    Dog = 2
    Hamster = 3

    @staticmethod
    def get_type(type_id):
        if type_id == 1:
            return PetType.Cat
        elif type_id == 2:
            return PetType.Dog
        elif type_id == 3:
            return PetType.Hamster
        else:
            return None

class PetCreator(Creator):
    def create_new_pet(self, pet_type):
        if pet_type == PetType.Cat:
            return Cat()
        elif pet_type == PetType.Dog:
            return Dog()
        elif pet_type == PetType.Hamster:
            return Hamster()
        else:
            return None
