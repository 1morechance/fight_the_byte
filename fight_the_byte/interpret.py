'''!@brief Интерпретирует код игроков
'''
from check_win import check_winner

def interpretation(stack_1, stack_2, word, main_window):
    '''!@brief Интерпретирует код игроков
        @param[out] output_string - содержит слово, полученное после выполнения
        игрока
    '''
    for num in range(len(stack_1)):
        try:
            stack_1[num].action()
            if (check_winner(word)):
                return 1
        except RuntimeError as err:
            main_window.setup_results()
            main_window.output_window.setText("Player '" + main_window.players_dict[1] + "' disqualificated by :\n" + str(err))
            return 0
        try:
            stack_2[num].action()
            if (check_winner(word)):
                return 2
        except RuntimeError as err:
            main_window.setup_results()
            main_window.output_window.setText("Player '" + main_window.players_dict[2] + "' disqualificated by :\n" + str(err))
            return 0
    return 0
