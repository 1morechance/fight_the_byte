'''!@brief сердце программы
Randomizer - генератор рандомных карточек
Контролируемый рандом 

Генерирует 8 карточек
'''

from random import randint, uniform
import pandas as pd

from cards import *



def generate_vars(m):
    '''!@brief Генерация карточек
        @details Функция генерирует имена переменных на первом драфте.
        Имя переменной - случайная буква из simple_names
        @params simple_names - буквы для имен карточек
        @params length - количество букв
        @params names_list - массив сгенерированных карточек
        @params[out] vars_data - DataFrame
        @params var - имя текущей созданной карточки

    '''
    simple_names = 'qwertyuiopasdfghjklzxvbnm'
    length = len(simple_names) - 1

    names_list = []
    for i in range(m):
        var = simple_names[randint(0, length)]
        while var in names_list:
            var = simple_names[randint(0, length)]
        names_list.append(var)

    vars_data = pd.DataFrame({'Type': [None for i in range(m)],       # Var OR Pointer
                              'Init': [False for i in range(m)],      # True OR False
                              'Value': [None for i in range(m)],      # <Value> OR None
                              'Putchar': [False for i in range(m)]},  # True OR False
                             index=names_list)
    vars_data.index.name = 'Variables'
    return vars_data


# # Проверка: присвоено ли какое-то значение перерменной
# def has_value(cell):
#     if cell is None:
#         return False
#     else:
#         return True




def select_type(choices):
    '''!@brief Функция выбора ("взвешенного" - неравновероятных событий)

        1) На основании данных DataFrame или абсолютно случайно
        2) Будет ли это переменная или указатель
        3) Будет ли это просто init AND/OR declaration
        @param[out] key - ключ к выбору типа

    '''
    amount = sum(choices.values())
    seed = uniform(0, amount)
    current = 0
    for key, value in choices.items():
        current += value
        if current >= seed:
            return key


def count_vars(vars_data):
    '''!@brief Фукнция подсчета количества VAR-ов
        @param[out] counter - счетчик
    '''
    counter = 0
    for i in range(len(vars_data.index)):
        if vars_data.iloc[i, 0] == 'VAR':
            counter += 1
    return counter


 
def create_card(vars_data, word):
    '''!@brief Функция "хитрой" генерации карточки (на основании данных DataFrame)
        @param index_main - рандомное число
        @param var_name - имя созданной карточки
        @param[out] vars_data, Card - Возвращает сгенерированную карточку 
    '''
    index_main = randint(0, len(vars_data.index) - 1)
    var_name = vars_data.index[index_main]

    if count_vars(vars_data) >= 2*len(word) - 2:  # Переменных больше МИНИМУМА (услвоного)
        vars_data, Card = create_random_card(vars_data, word)  # temporary
    else:
    # Если переменных достаточно мало (именно VAR)
    # НЕ будет создаваться указателей, пока сюда заходит программа
        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'

        word_symbol = word[randint(0, len(word) - 1)]
        # Шансы соотвественно 30%, 30%, 25% и 15%
        card_choice = {'init': 25, 'declaration': 25, 'i+d': 20, 'value-value': 15, 'putchar': 15}
        if select_type(card_choice) == 'init':
            Card = Init_card(char_name=var_name, char_value=word_symbol)

            vars_data.loc[var_name, 'Value'] = word_symbol

        elif select_type(card_choice) == 'declaration':
            Card = Declaration_card(char_name=var_name)

            vars_data.loc[var_name, 'Init'] = True

        elif select_type(card_choice) == 'i+d':
            Card = Init_declaration_card(char_name=var_name, char_value=word_symbol)

            vars_data.loc[var_name, 'Init'] = True
            vars_data.loc[var_name, 'Value'] = word_symbol

        elif select_type(card_choice) == 'value-value':
            index_add = randint(0, len(vars_data.index) - 1)
            while index_add == index_main:
                index_add = randint(0, len(vars_data.index) - 1)
            second_var = vars_data.index[index_add]
            Card = Value_to_value_card(left_name=var_name, right_name=second_var)

            if (vars_data.loc[second_var, 'Value'] is not None):
                vars_data.loc[var_name, 'Value'] = vars_data.loc[second_var, 'Value']

        elif select_type(card_choice) == 'putchar':
            Card = Putchar_card(char_name=var_name)

            vars_data.loc[var_name, 'Putchar'] = True
            
    return vars_data, Сard




def create_random_card(vars_data, word):
    '''!@brief Генерация очередной карточки (абсолютно случайно)
        @param[in] vars_data, word - массив сгенерированных карточек и слово
        @param[out] vars_data, Card - возвращает сгенерированную карточку
    '''
    index_main = randint(0, len(vars_data.index) - 1)
    var_name = vars_data.index[index_main]

    while vars_data.loc[var_name, 'Type'] == 'POINTER':
        index_main = randint(0, len(vars_data.index) - 1)
        var_name = vars_data.index[index_main]

    class_amount = 4  # Пока не все реализовано
    seed = randint(0, class_amount)

    # Топорно, согласен (beta)
    # Пока без поинтеров
    if seed == 0:
        word_symbol = word[randint(0, len(word) - 1)]
        Card = Init_card(char_name=var_name, char_value=word_symbol)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        vars_data.loc[var_name, 'Value'] = word_symbol

    if seed == 1:
        Card = Declaration_card(char_name=var_name)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        vars_data.loc[var_name, 'Init'] = True

    if seed == 2:
        word_symbol = word[randint(0, len(word) - 1)]
        Card = Init_declaration_card(char_name=var_name, char_value=word_symbol)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        vars_data.loc[var_name, 'Init'] = True
        vars_data.loc[var_name, 'Value'] = word_symbol

    if seed == 3:
        index_add = randint(0, len(vars_data.index) - 1)
        while index_add == index_main:
            index_add = randint(0, len(vars_data.index) - 1)
        second_var = vars_data.index[index_add]
        Card = Value_to_value_card(left_name=var_name, right_name=second_var)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        if vars_data.loc[second_var, 'Value'] is not None:
            vars_data.loc[var_name, 'Value'] = vars_data.loc[second_var, 'Value']


    if seed == 4:
        Card = Putchar_card(char_name=var_name)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'

        vars_data.loc[var_name, 'Putchar'] = True


    return vars_data, Card



def analyse_data(vars_data, word, n):
    '''!@brief Функция генерации списка карточек на драфте
        @param[in] vars_data, word - слово, которое надо распечатать игроку
        @param[out] vars_data, cards_array - массив сгенерированных карточек
    '''
    cards_array = []
    type_of_generation = {'normal': 90, 'random': 10}  # 90% и 10% соотвественно
    for i in range(n):
        if select_type(type_of_generation) == 'normal':  # Поскольку "хитро" нельзя пока
            vars_data, Card = create_random_card(vars_data, word)
        elif select_type(type_of_generation) == 'random':
            vars_data, Card = create_random_card(vars_data, word)
        cards_array.append(Card)
    return vars_data, cards_array


# Возможная идея (продолжение не получила, но вдруг еще пригодится)
# Функия вычисляет seed: 16-ричное число, которое указывает, за что отвечает та или иная переменная
#   1 - переменная только объявлена
#   2 - переменной только присвоено значение
#   3 - переменная объявлена и ей присвоено значение
#   4 - указатель объявлен
#   5 -
# def calc_seed(vars_data):
#     seed = 0;
#     for i in range():
#
#
# def decode_seed():
#     return seed





def generate_draft(n, vars_data, word):
    '''!@brief Функция, генерирущая очередной драфт карточек (вызыввается в main.py)
        @param[in] n -- Количество карточек на драфте
        @param[in] vars_data -- DataFrame (pandas) с информацией переменных и указателях
        @param[in] word -- слово, которое по заданию надо распечатать игроку
        @param[out] output_tuple - кортеж с измененнными DataFrame & список карточек (в таком порядке!)
    '''
    if len(vars_data.index) == 0:
        # Число от балды, возможно стоит придумать, как его вычислять
        vars_amount = 2*len(word) + 2
        vars_data = generate_vars(vars_amount)

    output_tuple = analyse_data(vars_data, word, n)
    return output_tuple
