"""
Урок 2. Знакомство с Python. Продолжение
1 - Напишите программу, которая принимает на вход вещественное 
число и показывает сумму его цифр. Учтите, что числа могут быть 
отрицательными

Пример:

67.82 -> 23
0.56 -> 11

"""
from os import system
system('cls')

# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = float(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Это не число!")
#     return number


# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum


# num = InputNumbers("Введите число: ")

# print(f"Сумма цифр = {sumNums(num)}")

"""
2 - Напишите программу, которая принимает на вход число N и 
выдает набор произведений (набор - это список) чисел от 1 до N.
Не используйте функцию math.factorial.
Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

"""


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")

"""
3 - Палиндромом называется слово, которое в обе стороны читается 
одинаково: "шалаш", "кабак".
А еще есть палиндром числа - смысл также в том, чтобы число в 
обе стороны читалось одинаково, но есть одно "но".
Если перевернутое число не равно исходному, то они складываются и 
проверяются на палиндром еще раз.
Это происходит до тех пор, пока не будет найден палиндром.
Напишите такую программу, которая найдет палиндром введенного 
пользователем числа.

"""


"""

4 - Реализуйте выдачу случайного числа
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
Учтите, что есть диапазон: от(минимальное) и до (максимальное)

"""

