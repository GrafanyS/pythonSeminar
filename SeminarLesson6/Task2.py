"""
Найти сумму чисел списка стоящих на нечетной позиции
"""
from functools import reduce


lst = [5, 8, 7, 0, 6, -4, 9]

print(reduce(lambda s, i: s+lst[i] if i % 2 else s, range(len(lst)), 0))
