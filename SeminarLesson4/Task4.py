"""
<<<<<<< HEAD
Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
При расшифровке происходит обратная операция. К примеру, слово `"абба"` можно зашифровать `"бввб"` - сдвиг на 1 вправо. 
=======
Шифр Цезаря - это способ шифрования, где каждая буква смещается 
на определенное количество символов влево или вправо. 
При расшифровке происходит обратная операция. К примеру, 
слово `"абба"` можно зашифровать `"бввб"` - сдвиг на 1 вправо. 
>>>>>>> 4a85a1f30ca84be98aab909c07c2749feb93e328
`"вггв"` - сдвиг на 2 вправо, `"юяяю"` - сдвиг на 2 влево.

Сдвиг часто называют ключом шифрования.
Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.
"""

quest = input(
    'Вы хотите зашифровать или дешифровать ваше сообщение? ("зашифровать":1 "дешифровать":2) ')
alfhavit =\
    'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя\
        ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
file = open("SeminarLesson4/file_сaesar.txt", "a", encoding="utf-8")

"""функция зашифровать"""


def encryption(alfhavit):
    message = input("Введите сообщение, которое хотите зашифровать: ")
    direction = input(
        "Введите направление сдвига (например, 'вправо':1 'влево':2): ")
    number = int(input("Введите шаг сдвига: "))
    new_text = ''
    for i in message:
        place = alfhavit.find(i)
        if direction == '1':
            place_2 = place + number
            if i in alfhavit:
                new_text += alfhavit[place_2]
            else:
                new_text += i
        elif direction == '2':
            place_2 = place - number
            if i in alfhavit:
                new_text += alfhavit[place_2]
            else:
                new_text += i
    return new_text


"""функция дешифровать"""


def decryption(alfhavit):
    message = input("Введите сообщение, которое хотите дешифровать: ")
    direction = input(
        "Введите направление сдвига, которое использовали при шифровке (например, 'вправо':1 'влево':2): ")
    number = int(input("Введите шаг сдвига: "))
    new_text = ''
    for i in message:
        place = alfhavit.find(i)
        if direction == '1':
            place_2 = place - number
            if i in alfhavit:
                new_text += alfhavit[place_2]
            else:
                new_text += i
        elif direction == '2':
            place_2 = place + number
            if i in alfhavit:
                new_text += alfhavit[place_2]
            else:
                new_text += i
    return new_text


if quest == '1':
    new_message = encryption(alfhavit)
    file.write(new_message + '\n')
    file.close()
elif quest == '2':
    new_message = decryption(alfhavit)
    file.write(new_message + '\n')
    file.close()
else:
    print("ОШИБКА")
