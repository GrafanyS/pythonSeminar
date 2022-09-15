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

import json


FILE = "text.txt"
list_student = []               # пустой список
with open(FILE, "r") as f:      # открываем файл для чтения
    for line in f:              # для строки в открытом файле
        if '5' in line:         # если '5' в строке
            line = line.upper() # переводим в верхний регистр 
        list_student.append(line.replace('\n', '')) # добавляем и заменяем строки

with open(FILE, "w") as f:      # открываем файл для перезаписи
    for line in list_student:   # для строки в list_student 
        f.write(line + '\n')    # записываем строки


FILE1 ='list.json' 

def source_file():
    list_student_appraisals = {'Ангела Меркель': 5,
                  'Андрей Валетов': 5,
                  'Фредди Меркури': 3,
                  'Анастасия Пономарева': 4}

    with open(FILE1, 'w') as f:
        f.write(json.dumps(list_student_appraisals))


def main_prog():
    with open(FILE1, 'r') as f:
        apr = json.load(f)

    for i in apr.keys():
        if apr[i] > 4:
            print(i.upper())
