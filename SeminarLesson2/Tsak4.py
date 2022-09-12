"""
4 - Реализуйте выдачу случайного числа
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
Учтите, что есть диапазон: от(минимальное) и до (максимальное)
Домашнее задание отправляйте в виде ссылки на гит-репозиторий


"""

import time
print(
    'Реализуйте выдачу случайного числа (или алгоритм перемешивания списка) без использования библеотеки рандом')
time_string = str(time.time_ns())

list_nums = [2, 4, 6, 8, 10, 12, 26]
print(list_nums)

for i in range(0, len(list_nums)):
    for j in time_string:
        if int(j) < len(list_nums):
            list_nums[i], list_nums[int(j)] = list_nums[int(j)], list_nums[i]

print(list_nums)
