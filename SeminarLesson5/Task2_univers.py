"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) (доп) Подумайте как наделить бота ""интеллектом""
"""

import random


print(
    '"Игра с конфетами"\n'
    'В игре участвуют два игрока\n'
    'Первый ход определяется жеребьевкой.\n'
    'Игроки ходят, совершая ход друг после друга\n'
    'Правила игры\n'
    'У нас есть некоторое количество конфет\n'
    'За один ход можно забрать не более определенного количества конфет, о котором мы договоримся\n'
    'Тот, кому достанется последняя конфета - проиграл\n'
)

def check_input_int(candy_per_moves):
    while True:
        try:
            input_num = int(input(f'Ввеите число от 1 до {candy_per_moves}: '))
            if 0 < input_num < candy_per_moves + 1:
                return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')


def get_toss():
    toss = True
    r = random.randint(0, 1)
    if r == 0:
        toss = False
    return toss


def get_candy():
    while True:
        try:
            input_num = int(input('Ввеите число конфет: '))
            if input_num > 2:
                return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')


def get_candy_per_move(count_candy):
    while True:
        try:
            input_num = int(
                input(f'Ввеите число конфет, которое будем брать за раз, но не больше чем {(count_candy // 3)}: '))
            if 0 < input_num <= (count_candy // 3):
                return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')


def the_game_2(flags, count_candy, player1_name, player2_name):
    player1_move = 0
    count = 1
    while count_candy > 0:
        if flags:
            print(f'Ход игрока {player1_name}')
            player1_move = check_input_int(candy_per_move)
            count_candy -= player1_move
            print(f'Осталось {count_candy} конфет')
            flags = False
            count += 1
            if count_candy == 1:
                print(f'Игрок {player1_name} выиграл')
                break
        else:
            print(f'Ход игрока {player2_name}')
            player2_move = bot(candy_per_move, count_candy,
                               player1_move, count)
            print(player2_move)
            count_candy -= player2_move
            print(f'Осталось {count_candy} конфет')
            flags = True
            count += 1
            if count_candy == 1:
                print(f'Игрок {player2_name} выиграл')
                break


def the_game_1(flags, count_candy, player1_name, player2_name):
    while count_candy > 0:
        if flags:
            print(f'Ход игрока {player1_name}')
            player1 = check_input_int(candy_per_move)
            count_candy -= player1
            print(f'Осталось {count_candy} конфет')
            flags = False
            if count_candy == 1:
                print(f'Игрок {player1_name} выиграл')
                break
        else:
            print(f'Ход игрока {player2_name}')
            player2 = check_input_int(candy_per_move)
            count_candy -= player2
            print(f'Осталось {count_candy} конфет')
            flags = True
            if count_candy == 1:
                print(f'Игрок {player2_name} выиграл')
                break


def get_name():
    name = input('Введите ваше имя:')
    return name


def bot(candy_per_mov, count_candy, player1_move, count):
    if count == 1:
        if count_candy % (candy_per_mov + 1) == 0 or count_candy % (candy_per_mov + 1) == 1:
            bot_move = 1
        else:
            bot_move = (count_candy % (candy_per_mov + 1)) - 1
    else:
        if candy_per_mov * 2 + 2 >= count_candy > candy_per_mov + 1:
            bot_move = (count_candy - candy_per_mov) - 2
        elif count_candy <= candy_per_mov + 1:
            bot_move = count_candy - 1
        else:
            bot_move = (candy_per_mov + 1) - player1_move
    return bot_move


def chose_mode():
    while True:
        try:
            game_mod = int(input(
                f'Ввеите число 1 - для игры с другом или 2 - для игры против компьютера: '))
            if game_mod == 1:
                return 1
            elif game_mod == 2:
                return 2
        except ValueError:
            print('Вы ввели неправильное значение!')


game_mode = chose_mode()
candy_count = get_candy()
candy_per_move = get_candy_per_move(candy_count)
flag = get_toss()
if game_mode == 1:
    the_game_1(flag, candy_count, player1_name=get_name(),
               player2_name=get_name())
elif game_mode == 2:
    the_game_2(flag, candy_count, player1_name=get_name(),
               player2_name='Бот Васька')
