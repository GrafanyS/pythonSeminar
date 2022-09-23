"""
Задана натуральная степень n. Сформировать случайным образом 
список коэффициентов (значения от 0 до 100) многочлена и записать 
в файл многочлен степени k.
Пример:
- n=2 => 2*x² + 4*x + 5 = 0 или 
x² + 5 = 0 (коэф: []) или 10*x² = 0
Уточнения:
n - это степень икса первого элемента полинома
при n =3 => 5*x*3 + 18*x2 + 7*x + 19 = 0 - 
коэффициенты = [5,18,7,19]
при n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) 
или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
при n=10 => 56 * x*10 = 0
коэффициенты - это числа перед элементами полинома.
коэффициенты могут быть нулем, кроме первого

"""

"""
Напишите программу вычисления арифметического выражения заданного
строкой.
Используйте операции +,-,/,. приоритет операций стандартный.
Дополнительное задание: Добавьте возможность использования скобок,
меняющих приоритет операций
*Пример:
2+2 => 4;
1+2*3 => 7;

10/2*5 => 25;
10 * 5 * => недостаточно числовых данных
-5 + 5 => 0
два + три => неправильный ввод: нужны числа
(2+((5-3)*(16-14)))/3 => 2

"""

expression = '-22+2'


def get_numbers(expression):
    numbers = []
    temp = ''
    expression += '='
    minus = -1 if expression[0] == '-' else 1
    expression = expression[1:] if expression[0] == '-' else expression
    for char in expression:
        if char.isdigit():
            temp += char
        else:
            numbers.append(temp)
            temp = ''
    numbers = list(filter(lambda char: char.isdigit(), numbers))
    numbers[0] = f'-{numbers[0]}'
    return numbers


def get_operators(expression):
    return list(filter(lambda char: char in '+-*/', expression))


def check_alpha(expression):
    return not any(filter(lambda char: char.isalpha(), expression))


def check_expression(numbers: list, opers: list):
    return True if len(numbers) > len(opers) else False


if check_alpha(expression):
    numbers = get_numbers(expression)
    list_operators = get_operators(expression)
    if check_expression(numbers, list_operators):
        print(numbers, list_operators)
    else:
        print('Выражение неполное', numbers, list_operators)
else:
    print('Вы ввели буквы')

""""from functools import reduce

print(list(filter(lambda char: char.isdigit(), ['1', '2', 'f', '4'])))


print(reduce(lambda element_1, element_2: element_1+element_2, [ord(char) for char in 'python']))
"""
