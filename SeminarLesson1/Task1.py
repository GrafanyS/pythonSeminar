""" 
Урок 1. Знакомство с Python
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет

"""


def input_numbers(input_text):  # функция проверки на ввод числа
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def check_number(num):  # функция проверки на день недели
    if 6 <= num <= 7:
        print("Да")
    elif 0 < num < 6:
        print("Нет")
    else:
        print("число вне пределов 7 дней")


num = input_numbers("Введите число: ")
check_number(num)
