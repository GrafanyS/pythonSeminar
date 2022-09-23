"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
Входные и выходные данные хранятся в отдельных текстовых файлах

файл первый:
AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool

>файл второй:
сжатый текст.    
"""

data_file = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
file_1 = open("SeminarLesson4/file_1.txt", "w")
file_2 = open("SeminarLesson4/file_2.txt", "w")


def compression(data):
    encoding = ''
    prev_char = ''
    count = ''
    if not data:
        return ''
    for i in data:
        if i != prev_char:
            encoding += str(count) + prev_char
            count = 1
            prev_char = i
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def recovery(data):
    decode = ''
    count = ''
    for i in data:
        if i.isdigit():
            count += i
        else:
            decode += i * int(count)
            count = ''
    return decode


file_1.write(recovery(compression(data_file)))
file_2.write(compression(data_file))
file_1.close()
file_2.close()
