class Counter:
    def __init__(self):
        self.value = 0
        self.used = False

    def add(self):
        self.value += 1

    def __enter__(self):
        if self.used:
            raise RuntimeError("Ресурс уже использован")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.used = True
        if exc_type is not None:
            print("Исключение обработано:", exc_type, exc_value)
        else:
            print("Ресурс успешно освобожден")
