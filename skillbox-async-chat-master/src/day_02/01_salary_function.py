"""
Пример программы для работы с функциями (аналог файла 01_hours_salary.py)

Аргументы
- стоимость часа в руб
- количество дней в руб

Сделать
- функцию, которая вернет размер зарплаты в руб
"""
def MySalary(cost_hour: int, day_count: int):
    cost_day = cost_hour*8
    salary = cost_day*day_count*0.87
    return print(f"Вы заработали {salary} руб.")

a = int(input("Введите стоимость 1 часа работы >>>"))
b = int(input("Введите количество рабочих дней>>>"))

MySalary(a, b)