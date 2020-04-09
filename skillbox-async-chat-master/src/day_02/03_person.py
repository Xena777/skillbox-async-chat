"""
Пример программы для работы с ООП

Данные класса
- имя
- фамилия
- возраст
"""
class Man:
    name: str
    surname: str
    age: int

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

Petya = Man("Petya", "Veselov", 25)
