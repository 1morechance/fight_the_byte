'''!@brief Интерпретирует код игроков
'''
from check_win import check_winner
from cards import output_string

def interpretation(stack_1, stack_2, word):
    '''!@brief Интерпретирует код игроков
        @param[out] output_string - содержит слово, полученное после выполнения
        игрока
    '''
    
    print(output_string)
    try:
        for num in range(len(stack_1)):
            stack_1[num].action()
            if (check_winner(word, output_string)):
                return 1
            stack_2[num].action()
            if (check_winner(word, output_string)):
                return 2
    except RuntimeError as err:
        print(err)
    return 0
