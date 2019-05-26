from cards import*
from randomizer import generate_draft
from pandas import DataFrame
from check_win import check_winner

# Учёт переменных общий и ведется в файле cards

# Стеки с кодом каждого игрока
stack_player_1 = []
stack_player_2 = []

HAND_SIZE = 8
WIN_BY = 'лещ'

data = DataFrame()
hand = (generate_draft(HAND_SIZE, data, WIN_BY))[1]

# Когда ход завершен, выполняется интерпретация
# По одной строчке
# Начиная с игрока который начинал игру

win = 0
LEFT_PLAYER = 1
RIGHT_PLAYER = 2

# В переменную current_out подается текст из поля вывода
try:
    for num in range(len(stack_player_1)):
        stack_player_1[num].action()
        if (check_win(current_output, WIN_BY)):
            win = LEFT_PLAYER
        stack_player_2[num].action()
        if (check_win(current_output, WIN_BY)):
            win = RIGHT_PLAYER
except RuntimeError as err:
    print(err)
