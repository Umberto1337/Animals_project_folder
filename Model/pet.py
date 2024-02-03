from abc import ABC, abstractmethod
from datetime import datetime

class Pet(ABC):
    def __init__(self):
        self.pet_id = 0
        self.name = ""
        self.birthday = None

    def set_pet_id(self, pet_id):
        self.pet_id = pet_id

    def get_pet_id(self):
        return self.pet_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_birthday(self, date):
        self.birthday = date

    def get_birthday_date(self):
        return self.birthday

    def get_birthday(self):
        return self.birthday.strftime("%d.%m.%Y")

    @abstractmethod
    def __str__(self):
        pass
