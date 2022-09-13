"""
print(''.join(list(filter(lambda char: char.isdigit(), num))))

"""


# def random(_min: int, _max: int) -> int:
#     '''
#     Генерация случайного числа
#     params:
#     min - начало диапазона
#     max - конец диапазона
#     '''
#     d = _max - _min  # 9
#     ms = datetime.datetime.today().microsecond / (10 ** 6)
#     #print(f'{ms=}')
#     return _min + math.ceil(d * ms)


'''
1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
['апап4', 'fdgg3', 'fgdf', '6', 'fg24'] - ищем 24 - найдено на 4 индексе



'''
# list_of_str = ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']
#
# number = int(input("Введите число: "))
# position_of_number = -1
# tem_position = -1
# counter = 0
# for elem in list_of_str:
#     tem_position = elem.find(str(number))
#
#     if tem_position != -1:
#         position_of_number = tem_position
#         break
#     counter += 1
# if tem_position != -1:
#     print(list_of_str,f"искали{number} ->", counter)
# else:
#     print(list_of_str, f"искали{number} ->а его нет!")

'''
2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1

'''
list_of_anytypes1 = ["qwe", "asd", "zxc",
                     "qwe", "ertqwe"]  # , ищем: "qwe", ответ: 3
list_of_anytypes2 = ["йцу", "фыв", "ячс", "цук",
                     "йцукен", "йцу"]  # , ищем: "йцу", ответ: 5
list_of_anytypes3 = ["йцу", "фыв", "ячс",
                     "цук", "йцукен"]  # , ищем: "йцу", ответ: -1
list_of_anytypes4 = ["123", "234", 123, "567"]  # , ищем: "123", ответ: -1
list_of_anytypes5 = []  # , ищем: "123", ответ: -1

user_sub_str = input("Введите строку: ")  # чисто для ошибки в переводе


def find_my_substring(list_of_types, my_substring, list_of_str=None, number=None):
    position_of_number = -1
    tem_position = -1
    counter = 0
    for elem in list_of_types:
        if (type(elem)) is str:
            tem_position = elem.find(str(number))
            if tem_position != -1:
                position_of_number = tem_position
                break
        else:
            continue
        counter += 1

    if tem_position != -1:
        print(list_of_str, f"искали {number} -> его позиция", counter)
    else:
        print(list_of_str, f"искали {number} -> а его нет! ")



'''
3.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''
# dictionary = {}
# n=int(input('Введите число= '))
# for i in range(1, n+1):
#     dictionary[i]=3*i+1
# print(dictionary)

