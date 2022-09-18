"""
1 -Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

    'абвгдейка - это передача' = >" - это передача"        
"""


my_text = 'Напишите программу, удаляющую из текста все слова, содержащие ""абв""'
print(my_text)

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)


my_text = 'абвгдейка - это передача'

my_text = del_some_words(my_text)
print(my_text)
