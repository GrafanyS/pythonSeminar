import random
from os import system
from random import randint

# system('clear')

# print("Программа, которая будет преобразовывать десятичное число в двоичное.")
#
# def dec_to_bin(number):
#     result = ""
#     temp = number % 2
#     if (temp == 0):
#         result = "0" + result
#         number = number / 2
#     elif (temp == 1):
#         result = "1" + result
#         number = (number - 1) / 2
#     if (number != 1):
#         return result + dec_to_bin(number)
#     else:
#         result = "1" + result
#         return result
#
# print(f'Число 45 в двоичном виде = {dec_to_bin(45)}')
# print(f'Число 3 в двоичном виде = {dec_to_bin(3)}')
# print(f'Число 2 в двоичном виде = {dec_to_bin(2)}')
'''
1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
В качестве символа-разделителя используйте пробел.
'''
# line = '1, 2, 3, 4, 5'
# list = []

# for i in range(len(line)):
#     if line[i] != ',' and line[i] != ' ':
#         list.append(int(line[i]))

# print(*list)
# print(f'Min: {min(list)}')
# print(f'Max: {max(list)}')

"""
2. Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел. 
НОК - наименьшее общее кратное, которое делится и на первое, и на второе число. 
 

"""

# def lcm(a, b):
#     lcm.multiple = lcm.multiple + b
#     if (lcm.multiple % a == 0) and (lcm.multiple % b == 0):
#         return lcm.multiple
#     else:
#         lcm(a, b)
#     return lcm.multiple

# lcm.multiple = 0
# a = int(input("Ввендите первое чило: "))
# b = int(input("Введите второе число: "))
# if (a > b):
#     LCM = lcm(b, a)
    
# else:
#     LCM = lcm(a, b)
    
# print(f'НОК {LCM}')
'''
2
'''
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# def NOD(a,b):
#     if a % b == 0:
#         return b
#     elif b % a == 0:
#         return a
#     elif a > b:
#         return NOD(a%b, b)
#     else:
#         return NOD(b%a, a)

# def NOK(a, b):
#     return  a*b / NOD(a, b)
# print(int(NOK(a, b)))
'''
2
'''
# i = min(a, b)
# while True:
#     if i % a == 0 and i % b == 0:
#         break
#     i += 1
# print(i)

"""
3. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
Число N вводится пользователем. Позиции хранятся в файле file.txt в одной строке одно число
Позиции в файл вам нужно программно положить в файл в зависимости от выбранного N: если пользователь введет двойку,
то в файле вряд ли будут индексы 5 или 16.
В решении должны быть и запись в файл, и чтение из файла.
"""

def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2*number)}\n")


def read_file():
    with open('file.txt', 'r') as data:
        indexs = list(map(int, data.readlines()))
    return indexs

# улучшение


n = int(input("Введите число N: "))
lst_number = [i for i in range(-n, n+1)]
write_file(n)
lst_index = read_file()
prod = 1
for i in range(len(lst_index)):
    prod *= lst_number[lst_index[i]]
print(f"Результат равен = {prod}")
