"""
Урок 2. Знакомство с Python. Продолжение
1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

Пример:

67.82 -> 23
0.56 -> 11

"""

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
            if is_minus:
                coord *= -1
            int_test = False
        elif coord.isdecimal():
            coord = float(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else:
            print("Not a number , try again")
    return coord
print('Используем программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
number = str(input_number("Введите число : "))

result = 0
for i in number:
    if i.isdigit():
        result = result+int(i)

print(f"Сумма цифр введенного числа ({number}) равняется: {result}")
