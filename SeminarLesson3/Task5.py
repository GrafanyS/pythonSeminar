"""
5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
Решение оформлять в виде функций
По возможности добавляйте docstring

"""
# Вариант через список чисел фибоначчи
# Функция для получения числа фибоначчи по его индексу
def fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# Получаем обыкновенный список чисел фибоначчи в зависиммости от введенного количества
def get_fibos_list(num):
    result_list = []
    for i in range(1, num + 1):
        result_list.append(fibo(i))
    return result_list

# Получаем список чисел фибоначчи для отрицательных и положительных чисел
def get_negafibo(list):
    result = []
    for item in range(len(list)):
        if ((len(list) - item) % 2 == 0):
            result.append(list[len(list) - item - 1] * -1)
        else:
            result.append(list[len(list) - item - 1])
    result.append(0)
    for item in range(len(list)):
        result.append(list[item])
    return result


print("Введите целое число: ")
num = int(input())
print(
    f'Для k = 8 список Негафибоначчи =>  {get_negafibo(get_fibos_list(num))}')

# Второй вариант через рекурсию
# функция fibonacci рекурсией
def fibonacci(n):
    if n == 1 or n == 2:    # Если n = 1, или n = 2, вернуть в вызывающую ветку единицу, 
                            # так как первый и второй элементы ряда Фибоначчи равны единице.
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Получаем список чисел фибоначчи для отрицательных и положительных чисел
def negafibonacci(num):
    negafibonacci = list()
    for i in range(-num, num + 1):
        if i < 0:
            '''
            Функция abs() — это встроенная функция, возвращающая абсолютное значение числа. 
            Она принимает целые, с плавающей точкой и комплексные числа на вход.
            abs(x) вычисляет абсолютное значение аргумента x
            float absolute value.
            '''            
            negafibonacci.append(-fibonacci(abs(i)))
        elif i == 0:
            negafibonacci.append(0)
        else:
            negafibonacci.append(fibonacci(i))
    return negafibonacci


print("Введите целое число: ")
num = int(input())
print(f'Для k = {num} список Негафибоначчи => {negafibonacci(num)}')
