"""
Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
При расшифровке происходит обратная операция. К примеру, слово `"абба"` можно зашифровать `"бввб"` - сдвиг на 1 вправо. 
`"вггв"` - сдвиг на 2 вправо, `"юяяю"` - сдвиг на 2 влево.

Сдвиг часто называют ключом шифрования.
Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.
"""


file = open('message.txt', 'rt', encoding='utf-8')
message_file = ''.join(file.readlines())
message_file = message_file.lower().strip()
file.close()
# Создаем алфавит
alfavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# encrypted = ''  # создаем переменную для вывода итогового сообщения

message_crypto = open('message_crypto.txt', 'wt')


def crypto(renge):
    encrypted = ''
    for i in renge:
        encrypted += '*'
    for i in renge(len(encrypted)):
        if encrypted[i] in alfavit:
            string = string.replace(
                '*', alfavit[alfavit.index(encrypted[i]) - 6], 1)
        else:
            string = string.replace('*', encrypted[i], 1)
    return string


message_crypto.writelines(crypto(message_file))
print(crypto(message_crypto))
message_crypto.close()
# else:
    # for i in message:
    #     # Алгоритм для шифрования сообщения на английском
    #     mesto = alfavit_EU.find(i)
    #     new_mesto = mesto + smeshenie
    #     if i in alfavit_EU:
    #         itog += alfavit_EU[new_mesto]
    #     else:
            # itog += i


# print("Ваше сообщение:", encrypted)


# file = open("message.txt", "w", encoding="utf-8")
# message = file

# alfavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# encrypted = ''

# for i in message:
#     mesto = alfavit.find(i)
#     new_mesto = mesto + 1
#     if i in alfavit:
#         encrypted += alfavit[new_mesto]
#     else:
#         encrypted += i

# print("Ваше сообщение:", encrypted)
