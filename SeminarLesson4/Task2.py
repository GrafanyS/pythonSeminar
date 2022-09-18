"""
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов 
исходной последовательности. Не использовать множества.

[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
"""
from os import system
import numbers
import itertools
'''
Для Windows system('cls')
'''
system('cls') 
'''
Для Linux system('clear')
'''
# system('clear')

#  генератор целочисленного последовательного списка
def generate():
    for i in itertools.count(1):
        yield from [int(i)] * i

#  Функция ввода числа с проверкой на ввод числа
def input_numbers(n):  
    is_OK = False
    while not is_OK:
        try:
            number = int(input('Задайте последовательность чисел в кличестве: '))
            is_OK = True
        except ValueError:
            print("Это не целое число!")
    return number

# lst = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
# lst = list(map(int, input("Введите числа через пробел: ").split()))
# lst = [i * j for i in range(0, 4) for j in range(0, 3)]
lst = [*itertools.islice(generate(), input_numbers(numbers))]
print(f'Исходный список: {lst}')
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f'Список из неповторяющихся элементов: {new_lst}')
