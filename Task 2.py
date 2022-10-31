# Создайте программу для игры в ""Крестики-нолики"".

from operator import truediv

# создание пустого поля 3х3
def get_list():
    a = 3
    mas = []
    for i in range(a):
        mas.append(["_"] * a)
    return mas

# печать поля
def print_list(mas):
    for i in range(0, len(mas)):
        for j in range(0, len(mas[i])):
            print(mas[i][j], end=' ')
        print()

# Запросить ввод позиции для игрока.
def quest_input():
    row_column = (input(f'Игрок {current_player}, введите значение строки и столбца через пробел (от 0 до 2): ').split(" "))
    print(row_column)
    return row_column

# Проверить вхождение введенных позиций в диапазон размера массива.
def check_mas_range(row_column):
    row_i = int(row_column[0])
    column_j = int(row_column[1])
    if 0 <= row_i < 3 and 0 <= column_j < 3:
        return True
    else:
        print("неправильная позиция")
        return quest_input()

# Переключить игрока
def next_player(current_player):
    # Если должен выполнить ход другой игрок.
    if (current_player == 1):
        return 2
    else:
        return 1

# Ход игрока
def player_turn(current_player):
    # Если должен выполнить ход другой игрок.
    if (current_player == 1):
        player1(input_player_position, massiv)
    else:
        player2(input_player_position, massiv)

# ход игрока 1
def player1(row_column, mas):
    row_i = int(row_column[0])
    column_j = int(row_column[1])
    mas[row_i][column_j] = "x"
    print_list(mas)

# ход игрока 2
def player2(row_column, mas):
    row_i = int(row_column[0])
    column_j = int(row_column[1])
    mas[row_i][column_j] = "0"
    print_list(mas)

# проверить свободна ли позиция.
def check_mas_label(row_column, mas):
    row_i = int(row_column[0])
    column_j = int(row_column[1])
    if (mas[row_i][column_j] != "_"):
        print("Позиция занята, укажите другую.")
        quest_input()
    return True

# проверка свободных позиций
def check_free_possition(mas):
    for i in range(0, len(mas)):
        for j in range(0, len(mas[i])):
            if mas[i][j] == "_":
                return True
    return False

# проверка на победу
def check_win(mas):
    victories = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
    ] # варианты выигрыша (индексы i,j)
    for variant in victories:
        if mas[variant[0][0]][variant[0][1]] == mas[variant[1][0]][variant[1][1]] == mas[variant[2][0]][variant[2][1]] != "_":
            return True
        # if mas[variant[0][0]][variant[0][1]] == "x" and  mas[variant[1][0]][variant[1][1]] == "x" and mas[variant[2][0]][variant[2][1]] == "x":
        #     return True
        # if mas[variant[0][0]][variant[0][1]] == "0" and  mas[variant[1][0]][variant[1][1]] == "0" and mas[variant[2][0]][variant[2][1]] == "0":
        #     return True
    return False

current_player = 1  # флаг игрока
massiv = get_list()  # создание пустого поля
print_list(massiv)  # печать пустого поля
game_runned = True  # флаг игры
while (game_runned):  # пока Правда игра продолжается
    if check_free_possition(massiv) == False:  # есть ли еще свободные позиции
        print(f'Ничья.')
        break
    input_player_position = quest_input()  # запрос на ввод строки/столбца
    # проверка вхождения чисел в диапозон 0-2
    if check_mas_range(input_player_position):
        if check_mas_label(input_player_position, massiv):  # свободна ли позиция
            player_turn(current_player)  # ход игрока
            is_win = check_win(massiv)  # проверить - выиграл?
            if (is_win):
                game_runned = False
                print(f'Победил игрок {current_player}')
                break
            if (game_runned):
                current_player = next_player(
                    current_player)  # переключить игрока


