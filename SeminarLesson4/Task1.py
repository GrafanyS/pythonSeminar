"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

    N = 20 -> [2,5]
    N = 30 -> [2, 3, 5]
"""


# def primfacs(num):
#    i = 2
#    numbers = []
#    while i * i <= num:
#        while num % i == 0:
#            numbers.append(i)
#            num = num / i
#        i = i + 1
#    if num > 1:
#        numbers.append(num)
#    return numbers


# num = int(input("Введите число N: "))
# print(f'N = {primfacs(num)}')

num = int(input("Введите число: "))
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


n = int(input())
while n > 1:    
    i = 2
    f = 0
    while 1:        
        if n % i == 0:            
            n = n // i 
            print(i, end=' ') 
            f = 1 
            break 
        else:            
            i += 1 
    if f == 1:       
        continue 
print() 
