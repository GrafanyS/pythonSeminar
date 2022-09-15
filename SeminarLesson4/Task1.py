"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

    N = 20 -> [2,5]
    N = 30 -> [2, 3, 5]
"""
# В примере N = 20 -> [2,5] есть ошибка, долно быть N = 20 -> [2,2,5]
# первый вариант
def primfacs(num):
   i = 2
   numbers = []
   while i * i <= num:
       while num % i == 0:
           numbers.append(i)
           num = num / i
       i = i + 1
   if num > 1:
       numbers.append(num)
   return numbers


num = int(input("Введите число N: "))
print(f'Простые множители числа {num} приведены в списке: {primfacs(num)}')

# второй вариант
num = int(input("Введите число N: "))
i = 2  # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")
