"""
 Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.

    ['python', 'c#']

    [1,2]

 Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.

        [(1,'PYTHON'), (2,'C#')]

Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.

    [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
    [(1,'PYTHON'), (102,'C#')]

Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: [UTF-8 code page](<https://www.charset.org/utf-8>)

Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
[Как текст хранится в компьютере](<https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6>)
"""
languages = [
    'python', 
    'c#', 
    'PHP', 
    'Java', 
    'Go', 
    'JavaScript',
    'PHP',
    'C++',
    'C',
    'Kotlin',
    'Delphi'
    ]
numbers = [i for i in range(1, len(languages)+1)]

combine_list = list(zip(numbers, [i.upper() for i in languages]))


def summ(x):
    return (sum([ord(str(i)) for i in x[1]]), x[1])

def foo(x):
    return x[0] % 2 == 0


combine_list = list(filter(foo, map(summ, combine_list)))
print(combine_list)