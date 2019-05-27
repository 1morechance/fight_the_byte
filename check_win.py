'''!@brief Определяет вывел ли игрок нужное слово
    @param[out] WIN = 1, NO_WIN = 0 - Константы
'''

WIN = 1
NO_WIN = 0

def check_winner(word, current_state):
    '''!@brief Функция определяет вывел ли игрок нужное слово
        @param i - счетчик
        @param cut - текущее слово игрока
        @param word - заданное слово
    '''
    i = 0
    while (i + len(word) - 1 < len(current_state)):
        cut = current_state[i:i + len(word)]
        if (cut == word):
            return WIN
        i += 1
    return NO_WIN

print(check_winner("fook", ""))
