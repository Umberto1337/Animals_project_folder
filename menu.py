from Model.pets import PetType, PetCreator
from Counter.counter import Counter

class Menu:
    @staticmethod
    def display_menu():
        print("1. Завести новое животное")
        print("2. Определить животное в правильный класс")
        print("3. Увидеть список команд, которые выполняет животное")
        print("4. Обучить животное новым командам")
        print("5. Выйти из программы")

    @staticmethod
    def get_user_choice():
        return input("Выберите действие (1-5): ")
