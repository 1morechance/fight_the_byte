'''!@brief Определяет вывел ли игрок нужное слово
    @param[out] WIN = 1, NO_WIN = 0 - Константы
'''
from cards import get_output

WIN = 1
NO_WIN = 0

def check_winner(word):
    '''!@brief Функция определяет вывел ли игрок нужное слово
        @param i - счетчик
        @param cut - текущее слово игрока
        @param word - заданное слово
    '''
    i = 0
    current_state = get_output()
    print(word, current_state, "states")
    while (i + len(word) - 1 < len(current_state)):
        cut = current_state[i:i + len(word)]
        if (cut == word):
            return WIN
        i += 1
    return NO_WIN