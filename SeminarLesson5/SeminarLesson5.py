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


# import random
# человек против человека

# n = 202
# m = 28
# print(f'Правила игры: \n1) На столе лежит {n} конфета.'
#       f'Играют два игрока, делая ход друг после друга. \n2) За один ход можно забрать не более {m} конфет.'
#       f'\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. \nУдачной игры!\n')
#
# first_player = input('Первый игрок, введите Ваше имя: ')
# second_player = input('Второй игрок, введите Ваше имя: ')
#
#
# def play_game(num, play):
#     count = 0
#     while num > 0:
#         size = int(input(f'\n{play[count % 2]}, Ваш ход: '))
#         if size > 28 or size <= 0:
#             attempt = 3
#             print('Ошибка!')
#             while attempt > 0:
#                 size = int(input(f'Осталось попыток {attempt}. Введите число от 1 до 28: '))
#                 if size > 28 or size <= 0:
#                     attempt -= 1
#                 else:
#                     break
#             if attempt == 0:
#                 return print('Вы проиграли!')
#         num = num - size
#         if num > 0:
#             print(f'Осталось конфет = {num}')
#         else:
#             print('Конфет больше нет.')
#         count += 1
#     return play[not count % 2]
#
#
# player = [first_player, second_player]
#
# wine = play_game(n, player)
# if not wine:
#     print('Нет победителя.')
# else:
#     print(f'Поздравляю! Победил {wine}.')


# from random import randint

# n = 202
# m = 28


# def human():
#     first_player = input('Первый игрок, введите Ваше имя: ')
#     second_player = input('Второй игрок, введите Ваше имя: ')

#     def play_game(num, play):
#         count = 0
#         while num > 0:
#             size = int(input(f'\n{play[count % 2]}, Ваш ход: '))
#             if size > 28 or size <= 0:
#                 attempt = 3
#                 print('Ошибка!')
#                 while attempt > 0:
#                     size = int(
#                         input(f'Осталось попыток {attempt}. Введите число от 1 до 28: '))
#                     if size > 28 or size <= 0:
#                         attempt -= 1
#                     else:
#                         break
#                 if attempt == 0:
#                     return print('Вы проиграли!')
#             num = num - size
#             if num > 0:
#                 print(f'Осталось конфет = {num}')
#             else:
#                 print('Конфет больше нет.')
#             count += 1
#         return play[not count % 2]

#     players = [first_player, second_player]

#     winner = play_game(n, players)
#     if not winner:
#         print('Нет победителя.')
#     else:
#         print(f'Поздравляю! Победил {winner}.')
#     return


# def bot():
#     player = input('Введите Ваше имя: ')
#     bot_player = 1

#     def play_game_with_bot(num, play):
#         count = 0
#         while num > 0:
#             count = count % 2
#             if count == 1:
#                 num = randint(1, 29)
#                 print(f'\n{bot_player}Ходит бот: {num}')
#                 num = num - num
#                 if num > 0:
#                     print(f'Осталось конфет = {num}')
#                 else:
#                     print('Конфет больше нет.')
#             if count == 0:
#                 size = int(input(f'\n{play}, Ваш ход: '))
#                 if size > 28 or size <= 0:
#                     attempt = 3
#                     print('Ошибка!')
#                     while attempt > 0:
#                         size = int(
#                             input(f'Осталось попыток {attempt}. Введите число от 1 до 28: '))
#                         if size > 28 or size <= 0:
#                             attempt -= 1
#                         else:
#                             break
#                     if attempt == 0:
#                         return print('Вы проиграли!')
#                 num = num - size
#                 if num > 0:
#                     print(f'Осталось конфет = {num}')
#                 else:
#                     print('Конфет больше нет.')
#             count += 1
#         return play[not count % 2]

#     play_game_with_bot(n, player)

#     player = [player, bot_player]
#     winner = play_game_with_bot(n, player)
#     if not winner:
#         print('Нет победителя.')
#     else:
#         print(f'Поздравляю! Победил {winner}.')
#     return


# result = int(input(
#     'С кем вы хотите играть? Если с человеком, введите 1. Если с ботом, введите 2: '))
# if result == 1:
#     human()
# if result == 2:
#     bot()
# else:
#     print('Введите 1 или 2!')

# print(f'Правила игры: \n1) На столе лежит {n} конфета.'
#       f'Играют два игрока, делая ход друг после друга. \n2) За один ход можно забрать не более {m} конфет.'
#       f'\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. \nУдачной игры!\n')


from random import randint

# quantity = 202
# in_one_move = 28




# def get_number(input_string):
#     """
#     Проверка ввода на число
#     """
#     try:
#         num = int(input(input_string))
#         return num
#     except ValueError:
#         return get_number(input_string)


# quantity = abs(get_number("Введите количество конфет для игры(только цифры): "))
# in_one_move = abs(get_number("Введите количество за ход (только цифры): "))


# def human():
#     print('Игра с человеком!')
#     first_player = input('Первый игрок, введите Ваше имя: ')
#     second_player = input('Второй игрок, введите Ваше имя: ')

#     def playing_with_a_person(num, player):
#         count = 0
#         while num > 0:
#             size = int(input(f'\n{player[count % 2]}, Ваш ход: '))
#             if size > 28 or size <= 0:
#                 attempt = 3
#                 print('Ошибка!')
#                 while attempt > 0:
#                     size = int(input(f'Осталось попыток {attempt}. Введите число от 1 до 28: '))
#                     if size > 28 or size <= 0:
#                         attempt -= 1
#                     else:
#                         break
#                 if attempt == 0:
#                     return print('Вы проиграли!')
#             num = num - size
#             if num > 0:
#                 print(f'Осталось конфет = {num}')
#             else:
#                 print('Конфет больше нет.')
#             count += 1
#         return player[not count % 2]

#     players = [first_player, second_player]

#     winner = playing_with_a_person(quantity, players)
#     if not winner:
#         print('Нет победителя.')
#     else:
#         print(f'Поздравляю! Победил {winner}.')
#     return


# def bot():
#     print('Игра с ботом!')
#     player = input('Введите Ваше имя: ')
#     player_bot = 'Бот'
#     print(f'\nИмя бота:{player_bot}')

#     def play_game_with_bot(num, play):
#         count = 0
#         while num > 0:
#             count = count % 2
#             if count == 1:
#                 num = randint(1, 29)
#                 print(f'\nХодит бот: {num}')
#                 num = num - num
#                 counting(num, count, play)
#             if count == 0:
#                 size = int(input(f'\n{play}, Ваш ход: '))
#                 if size > 28 or size <= 0:
#                     attempt = 3
#                     print('Ошибка!')
#                     while attempt > 0:
#                         size = int(input(f'Осталось попыток {attempt}. Введите число от 1 до 28: '))
#                         if size > 28 or size <= 0:
#                             attempt -= 1
#                         else:
#                             break
#                     if attempt == 0:
#                         return print('Вы проиграли!')
#                 num = num - size
#                 counting(num, count, play)
#             count += 1

#     play_game_with_bot(quantity, player)


# def players_choice():
#     num = str(input('\nВведите слово ЧЕЛОВЕК, если хотите сыграть с человеком или БОТ, если с ботом: ').lower())
#     if num == 'человек':
#         rules()
#         human()
#     if num == 'бот':
#         rules()
#         bot()
#     if num != 'человек' and num != 'бот':
#         print('Можно ввести только ЧЕЛОВЕК или БОТ! Повторите попытку.')
#         players_choice()


# def rules():
#     print(f'Правила игры: \n1) На столе лежит {quantity} конфета.'
#           f'Играют два игрока, делая ход друг после друга. \n2) '
#           f'За один ход можно забрать не более {in_one_move} конфет.'
#           f'\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. \nУдачной игры!\n')


# def counting(num, count, player):
#     if num > 0:
#         print(f'Осталось конфет = {num}')
#     else:
#         print('Конфет больше нет.')
#         if count == 0:
#             print(f'\n{player}, примите наши поздравления, Вы выиграли!')
#         if count == 1:
#             print(f'\n{player}, Вы проиграли. Выиграл бот!')


# players_choice()
