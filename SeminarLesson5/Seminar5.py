# import numbers
# import random

# numbers = []
# for i in range(5):
#     finally
# f = list(filter(lambda i: False if not i % 2 else True, numbers))

"""
Задана натуральная степень n. Сформировать случайным образом 
список коэффициентов (значения от 0 до 100) многочлена и записать 
в файл многочлен степени n.
Пример:
- n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 (коэф: []) 
или 10*x² = 0


Уточнения:
n - это степень икса первого элемента полинома
при n =3 => 5*x*3 + 18*x**2 + 7*x + 19 = 0 - 
коэффициенты = [5,18,7,19]
при n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) 
или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
при n=10 => 56 * x*10 = 0

коэффициенты - это числа перед элементами полинома.
коэффициенты могут быть нулем, кроме первого


"""
import random
n = random.randint(1, 10)
print(f"Натуральная степень {n}")
list1 = [random.randint(1, 100)]
for i in range(1, n + 1):
    list1.append(random.randint(0, 100))
print(f"Список коэффициентов: {list1}")
list_x = []
for i in range(n + 1):
    list_x.insert(0, "x**" + str(i))
print(list_x)

polinom = list(zip(list1, list_x))
print(polinom)

s = str("")
for i, element in enumerate(polinom):
    for j in element:
        s = s + str(j)
    s = s + "+"

print(s)


# n = input_testing_number("Введите число целое: ")

# list_of_coef = random_list(0, 3, n)
# list_of_coef.append(random_list(1, 100, 1).pop())

# print(list_of_coef)
# str = f"{list_of_coef[n]}*x^{n}"
# i = n-1
# while i > 0:
#     if list_of_coef[i] == 0:
#         i -= 1
#         continue
#     elif i == 1:
#         str += f" + {list_of_coef[i]}*x"
#     else:
#         str += f" + {list_of_coef[i]}*x^{i}"
#     i -= 1
# else:
#     str += f" + {list_of_coef[0]}"
# print(str)

# with open("Our_polynom.txt", 'w', encoding='utf-8') as file:
#     print(str + " = 0", file=file)
