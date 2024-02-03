from menu import Menu
from pet_registry import PetRegistry
from Counter.counter import Counter
from datetime import datetime

def main():
    registry = PetRegistry()

    while True:
        Menu.display_menu()
        choice = Menu.get_user_choice()

        if choice == "1":
            pet_type = int(input("Введите тип животного (1 - Cat, 2 - Dog, 3 - Hamster): "))
            name = input("Введите имя животного: ")
            birthday = datetime.now()
            registry.add_pet(pet_type, name, birthday)
            print("Животное добавлено в реестр.")

        elif choice == "2":
            pet_id = int(input("Введите ID животного для определения класса: "))
            result = registry.determine_pet_class(pet_id)
            print(result)

        elif choice == "3":
            pet_id = int(input("Введите ID животного для просмотра команд: "))
            result = registry.show_pet_commands(pet_id)
            print(result)

        elif choice == "4":
            pet_id = int(input("Введите ID животного для обучения команде: "))
            command = input("Введите новую команду для обучения: ")
            result = registry.teach_pet_command(pet_id, command)
            print(result)

        elif choice == "5":
            registry.display_pet_registry()
        
        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 1 до 5.")

if __name__ == "__main__":
    # main() закомментировал, да бы сработал блок с try-except
    registry = PetRegistry()
    counter = Counter()

    try:
        with counter:
            pet_type = int(input("Введите тип животного (1 - Cat, 2 - Dog, 3 - Hamster): "))
            name = input("Введите имя животного: ")
            birthday = datetime.now()

            registry.add_pet(pet_type, name, birthday)
            print("Животное добавлено в реестр.")
            counter.add()

    except Exception as e:
        print("Произошло исключение:", e)