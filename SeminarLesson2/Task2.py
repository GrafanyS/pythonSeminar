"""
2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
Не используйте функцию math.factorial.
Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

"""
import random
# проверка ввода на число, но убирает минусовые значения


def input_number(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-", "")
        if coord.isdigit():
            coord = int(coord)
            if coord <= 0:
                print("Введите число больше нуля ( > 0)")
            else:
                int_test = False
        else:
            print("Вы ввели не число, попробуйте снова")
    return coord


def random_array_creation(elements, min_number, max_number):
    list_of_numbers = []
    for i in range(0, elements):
        list_of_numbers.append(random.randrange(min_number, max_number+1))
    return list_of_numbers

print('Используем программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')
#первый эллемент списка 1, затем по формуле - каждый эллемент - это предыдущий элемент, умноженный на index +1
num_N = input_number("Введите число N : ")
list_of_numbers = [1]
for i in range(1, num_N):
    list_of_numbers.append(list_of_numbers[i-1]*(i+1))
print(list_of_numbers)
