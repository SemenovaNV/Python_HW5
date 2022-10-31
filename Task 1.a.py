# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 201 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно
# взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

import random

# ввод числа от пользователя
def quest_input():
    num_candy = int(input(f'Игрок {current_player}, введите число конфет от 1 до 28: '))
    print(f'Игрок {current_player} ввел {num_candy}')
    if num_candy > 28 or num_candy <= 0:
        print(f'Введено неверное число, повторите ввод.')
        return quest_input()
    return num_candy

# ход бота
def bot_random_number():
    num_candy = random.randint(1, 28)
    print(f'Игрок {current_player} ввел {num_candy}')
    return num_candy

# игра
def game_candy(number_candies, num_candy):
    number_candies = number_candies - num_candy
    if number_candies < 0:
        number_candies = 0
    print(f'Осталось {number_candies} конфет')
    return number_candies

# проверка выигрыша
def win_check(turn):
    if turn <= 0:
        return True

# переключение игрока
def change_player(current_player):
    if current_player == 1:
        return 2
    return 1

number_candies = 201  # количество конфет в начале игры
print(f'В начале игры {number_candies} конфет')
current_player = random.randint(1, 2)  # рандомный первый ход 1 или 2 игрок
print(f'Ход {current_player} игрока')
game_runned = True  # флаг игры

while (game_runned):  # пока Правда игра продолжается
    if current_player == 1:
        number_entry = quest_input()  # ввод числа user
    if current_player == 2:
        number_entry = bot_random_number()  # ход бота рандомно
    number_candies = game_candy(number_candies, number_entry)  # ход игры
    is_win = win_check(number_candies)
    if is_win == True:
        print(f'Победил игрок {current_player}')
        game_runned = False
    current_player = change_player(current_player)