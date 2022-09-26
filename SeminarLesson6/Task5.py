"""
Найти произведение пар чисел в списке. Парой считаем первый и 
последний элемент, второй и предпоследний и т.д    
"""
lst = [2, 3, 4, 9, 1, 3]
length = len(lst)


print(list(map(lambda i: lst[i] * lst[length - i - 1], range(length // 2 + length % 2))))
