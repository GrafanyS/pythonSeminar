"""
2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]

"""

my_nums = [1, 2, 3, 4, 5, 6, 7]

'''
функция multiplication_elements которая
находит произведение пар чисел
'''
def multiplication_elements(origin_list):
    result_list = list()
    """
    делаю округление для того, чтобы в случае нечетного количества элементов в списке
    """
    lenght = round(len(origin_list)/2)
    '''
    "центральный" элемент перемножался сам на себя, как в примере
    '''
    for i in range(lenght):
        j = -i - 1
        mult = origin_list[i]*origin_list[j]
        result_list.append(mult)
    return result_list


print(multiplication_elements(my_nums))
