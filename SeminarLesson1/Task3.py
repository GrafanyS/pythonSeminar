"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон
возможных координат точек в этой четверти (x и y).
Напишите программу, которая принимает на вход координаты двух точек и находит
расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21

"""
from os import system
system('cls')

def input_numbers(x):  # функция проверки на ввод целго числа
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculate_length_segment(a, b):  # функция вычисления
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1])
                     ** 2) ** (0.5)  # Теорема Пифагора
    return lengthSegment


print("Введите координаты точки А")
pointA = input_numbers(2)
print("Введите координаты точки В")
pointB = input_numbers(2)

print(
    f"Длина отрезка: {format(calculate_length_segment(pointA, pointB)- 0.005, '.2f')}")
