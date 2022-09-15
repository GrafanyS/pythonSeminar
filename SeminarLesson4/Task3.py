'''
В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, 
которые имеют средний балл более «4».
Нужно перезаписать файл.
>Пример:

    Ангела Меркель 5
    Андрей Валетов 5
    Фредди Меркури 3
    Анастасия Пономарева 4

>Программа выдаст:

    АНГЕЛА МЕРКЕЛЬ 5
    АНДРЕЙ ВАЛЕТОВ 5
    Фредди Меркури 3
    Анастасия Пономарева 4
'''
"""первый вариант"""

FILE = "test.txt"
list_student = []               # пустой список
with open(FILE, "r", encoding='utf-8') as data:      # открываем файл для чтения
    for line in data:              # для строки в открытом файле
        if '5' in line:         # если '5' в строке
            line = line.upper()  # переводим в верхний регистр
        # добавляем и заменяем строки
        list_student.append(line.replace('\n', ''))

with open(FILE, "w", encoding='utf-8') as data:      # открываем файл для перезаписи
    for line in list_student:   # для строки в list_student
        data.write(line + '\n')    # записываем строки


"""вторй вариант"""

"""
Считывает из файла строки и возвращает список
"""


def read_file(file_path: str):
    res_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Сразу убираем перенос строки \n
            res_list.append(line.replace('\n', ''))

    return res_list


"""
Записывает в файл строки, заданные списком
"""


def write_file(file_path: str, list_str: str):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines('\n'.join(list_str))
    print('Закончил писать %s' % file_path)


"""
Ищет всех, у кого оценка больше 4 и переводит в верхний регистр
"""


def upper_file(ls: list):
    for i in range(0, len(ls)):
        index = len(ls[i])-1
        if int(ls[i][index]) > 4:
            ls[i] = ls[i].upper()


# write_into_file('file_students.txt')
str = read_file('file_students.txt')
upper_file(str)
write_file('file_students.txt', str)
