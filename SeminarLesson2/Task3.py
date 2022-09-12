"""
3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
Это происходит до тех пор, пока не будет найден палиндром.
Напишите такую программу, которая найдет палиндром введенного пользователем числа.


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
            if coord <= 0:
                print("Введите число больше нуля ( > 0)")
            else:
                int_test = False
        else:
            print("Вы ввели не число, попробуйте снова")
    return coord


print('Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.')
number_n = input_number("Введите N : ")

dict_of_numbers = {}

# как на семинаре
for i in range(1, number_n+1):
    dict_of_numbers[i] = (1+1/i)**i
print(dict_of_numbers)

result = 0

for i in dict_of_numbers:
    result += float(dict_of_numbers[i])
# ограничил двумя знаками после запятой
print(f"Сумма элементов равняется: {result:.2f}")
