"""
Пример программы для работы с условиями

Данные
- переменная со значением пароля password = 123123
- пользователь вводит строку с паролем

Сделать
- если пароль верный, вывести строку "Пароль верный"
- если пароль неверный, вывести строку "Ошибка"
"""

original_password = "123123"
user_password = input("Введите пароль >>> ")

if original_password == user_password:
    print("Верно")
else:
    print("Неверно")