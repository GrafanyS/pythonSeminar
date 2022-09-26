"""
Определить, присутствует ли в заданном списке строк, некоторое число
"""

lst = ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']

print(''.join(list(filter(lambda char: char.isdigit(), lst))))

number = 1
print(any(str(number) in s for s in lst))
