'''
Randomizer - генератор рандомных карточек
Контролируемый рандом ("подкрученый")

Генерирует N карточек
'''

from random import randint, uniform
import pandas as pd

from cards import *


# Функция генерирует имена переменных на первом драфте
#
#   Имя переменной - случайная буква из simple_names
def generate_vars(m):
    simple_names = 'qwertyuiopasdfghjklzxvbnm'
    length = len(simple_names) - 1

    names_list = []
    for i in range(m):
        var = simple_names[randint(0, length)]
        while var in names_list:
            var = simple_names[randint(0, length)]
        names_list.append(var)

    vars_data = pd.DataFrame({'Type': [None for i in range(m)],       # Var OR Pointer
                              'Declaration': [False for i in range(m)],      # True OR False
                              'Value': [None for i in range(m)],      # <Value> OR None
                              'Putchar': [False for i in range(m)]},  # True OR False
                             index=names_list)
    vars_data.index.name = 'Variables'
    return vars_data


# Функция выбора ("взвешенного" - неравновероятных событий)
# 1) На основании данных DataFrame или абсолютно случайно
# 2) Будет ли это переменная или указатель
# 3) Будет ли это просто init AND/OR declaration
def select_type(choices):
    amount = sum(choices.values())
    seed = uniform(0, amount)
    current = 0
    for key, value in choices.items():
        current += value
        if current >= seed:
            return key


# Функция подсчета количества VAR-ов
def count_vars(vars_data):
    counter = 0
    for i in range(len(vars_data.index)):
        if vars_data.iloc[i, 0] == 'VAR':
            counter += 1
    return counter


# Создание карточки переменной
def create_var_card(vars_data, word, var_name, index_main):
    if vars_data.loc[var_name, 'Type'] is None:
        vars_data.loc[var_name, 'Type'] = 'VAR'

    word_symbol = word[randint(0, len(word) - 1)]
    # Шансы соответственно 20%, 20%, 18%, 12% и 15%
    card_choice = {'init': 20, 'declaration': 20, 'i+d': 18,
                   'value-value': 12, 'i-another': 15, 'putchar': 15}

    choice = select_type(card_choice)
    if choice == 'init':
        Card = Init_card(char_name=var_name, char_value=word_symbol)

        vars_data.loc[var_name, 'Value'] = word_symbol

    elif choice == 'declaration':
        Card = Declaration_card(char_name=var_name)

        vars_data.loc[var_name, 'Declaration'] = True

    elif choice == 'i+d':
        Card = Init_declaration_card(char_name=var_name, char_value=word_symbol)

        vars_data.loc[var_name, 'Declaration'] = True
        vars_data.loc[var_name, 'Value'] = word_symbol

    elif choice == 'value-value':
        index_add = randint(0, len(vars_data.index) - 1)
        while index_add == index_main:
            index_add = randint(0, len(vars_data.index) - 1)
        second_var = vars_data.index[index_add]
        Card = Value_to_value_card(left_name=var_name, right_name=second_var)

        if vars_data.loc[second_var, 'Value'] is not None:
            vars_data.loc[var_name, 'Value'] = vars_data.loc[second_var, 'Value']

    elif choice == 'putchar':
        Card = Putchar_card(char_name=var_name)

        vars_data.loc[var_name, 'Putchar'] = True

    elif choice == 'i-another':
        index_add = randint(0, len(vars_data.index) - 1)
        while index_add == index_main:
            index_add = randint(0, len(vars_data.index) - 1)
        second_var = vars_data.index[index_add]
        Card = Init_card_another_var(left_name=var_name, right_name=second_var)

        vars_data.loc[var_name, 'Declaration'] = True
        if vars_data.loc[second_var, 'Value'] is not None:
            vars_data.loc[var_name, 'Value'] = vars_data.loc[second_var, 'Value']

        return vars_data, Card


def create_pointer_card(vars_data, var_name, p_name, index_p):
    if vars_data.loc[p_name, 'Type'] is None:
        vars_data.loc[p_name, 'Type'] = 'POINTER'

    card_choice = {'init': 18, 'declaration': 18, 'value-from': 16,
                   'value-value': 12, 'init-by': 14, 'p-p':10, 'putchar': 12}

    choice = select_type(card_choice)
    if choice == 'init':
        Card = Init_p_card(p_name=p_name, p_ref=var_name)

        if vars_data.loc[p_name, 'Type'] is None:
            vars_data.loc[p_name, 'Type'] = 'POINTER'
        vars_data.loc[p_name, 'Declaration'] = True
        if vars_data.loc[p_name, 'Value'] is not None:
            vars_data.loc[p_name, 'Value'] = vars_data.index[index_p]

    elif choice == 'declaration':
        Card = Declaration_p_card(pointer_name=p_name)

        vars_data.loc[p_name, 'Declaration'] = True

    elif choice == 'value-from':
        Card = Value_from_pointer(char_name=var_name, pointer_name=p_name)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        if vars_data.loc[p_name, 'Value'] is not None:
            vars_data.loc[var_name, 'Value'] = vars_data.loc[p_name, 'Value']

    elif choice == 'value-value':
        index_add = randint(0, len(vars_data.index) - 1)
        while index_add == index_p:
            index_add = randint(0, len(vars_data.index) - 1)
        second_p = vars_data.index[index_add]
        Card = Value_to_value_p_card(p_1=p_name, p_2=second_p)

        if vars_data.loc[second_p, 'Value'] is not None:
            vars_data.loc[p_name, 'Value'] = vars_data.loc[second_p, 'Value']

    elif choice == 'putchar':
        Card = Putchar_p_card(pointer_name=p_name)

        vars_data.loc[p_name, 'Putchar'] = True

    elif choice == 'init-by':
        Card = Init_by_pointer(char_name=var_name, pointer_name=p_name)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        if vars_data.loc[p_name, 'Value'] is not None:
            vars_data.loc[var_name, 'Value'] = vars_data.loc[p_name, 'Value']

    elif choice == 'p-p':
        index_add = randint(0, len(vars_data.index) - 1)
        while (index_add == index_p) or (vars_data.iloc[index_add, 1] == 'VAR'):
            index_add = randint(0, len(vars_data.index) - 1)
        second_p = vars_data.index[index_add]
        Card = Pointer_to_pointer(p_1=p_name, p_2=second_p)

        if vars_data.loc[second_p, 'Type'] is None:
            vars_data.loc[second_p, 'Type'] = 'POINTER'
        if vars_data.loc[second_p, 'Value'] is not None:
            vars_data.loc[p_name, 'Value'] = vars_data.loc[second_p, 'Value']


    return vars_data, Card


# Функция "хитрой" генерации карточки
# (на основании данных DataFrame)
def create_card(vars_data, word):
    # Находим указатель
    index_var = randint(0, len(vars_data.index) - 1)
    var_name = vars_data.index[index_var]
    while vars_data.loc[var_name, 'Type'] == 'POINTER':
        index_var = randint(0, len(vars_data.index) - 1)
        var_name = vars_data.index[index_var]

    # Находим указатель
    index_p = randint(0, len(vars_data.index) - 1)
    p_name = vars_data.index[index_p]
    while vars_data.loc[var_name, 'Type'] == 'VAR':
        index_p = randint(0, len(vars_data.index) - 1)
        p_name = vars_data.index[index_p]

    if count_vars(vars_data) >= 2*len(word) - 2:  # Переменных больше МИНИМУМА (условного)
        if vars_data.loc[var_name, 'Type'] is None:
            which_type = {'var': 40, 'pointer': 60}  # 40% и 60% соответсвенно
            if select_type(which_type) == 'var':
                vars_data, Card = create_var_card(vars_data, word, var_name, index_var)
            else:
                vars_data, Card = create_pointer_card(vars_data, var_name, p_name, index_p)
        else:
            # выбор для уже явной карточки && меньше, чем длина слова
            if vars_data.loc[var_name, 'Type'] == 'VAR':
                vars_data, Card = create_var_card(vars_data, word, var_name, index_var)
            elif vars_data.loc[var_name, 'Type'] == 'POINTER':
                vars_data, Card = create_pointer_card(vars_data, var_name, p_name, index_p)
    else:
        # Если переменных достаточно мало (именно VAR)
        # НЕ будет создаваться указателей, пока сюда заходит программа
        vars_data, Card = create_var_card(vars_data, word, var_name, index_var)

    return vars_data, Сard


# Генерация очередной карточки (абсолютно случайно)
def create_random_card(vars_data, word):
    # Находим указатель
    index_var = randint(0, len(vars_data.index) - 1)
    var_name = vars_data.index[index_var]
    while vars_data.loc[var_name, 'Type'] == 'POINTER':
        index_var = randint(0, len(vars_data.index) - 1)
        var_name = vars_data.index[index_var]

    # Находим указатель
    index_p = randint(0, len(vars_data.index) - 1)
    p_name = vars_data.index[index_p]
    while vars_data.loc[var_name, 'Type'] == 'VAR':
        index_p = randint(0, len(vars_data.index) - 1)
        p_name = vars_data.index[index_p]

    class_amount = 13
    seeds = {seed: 20 for seed in range(class_amount)}
    seed = select_type(seeds)

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
        vars_data.loc[var_name, 'Declaration'] = True

    if seed == 2:
        word_symbol = word[randint(0, len(word) - 1)]
        Card = Init_declaration_card(char_name=var_name, char_value=word_symbol)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        vars_data.loc[var_name, 'Declaration'] = True
        vars_data.loc[var_name, 'Value'] = word_symbol

    if seed == 3:
        index_add = randint(0, len(vars_data.index) - 1)
        while (index_add == index_var) or (vars_data.iloc[index_add, 1] == 'POINTER'):
            index_add = randint(0, len(vars_data.index) - 1)
        second_var = vars_data.index[index_add]
        Card = Value_to_value_card(left_name=var_name, right_name=second_var)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        if vars_data.loc[second_var, 'Type'] is None:
            vars_data.loc[second_var, 'Type'] = 'VAR'
        if vars_data.loc[second_var, 'Value'] is not None:
            vars_data.loc[var_name, 'Value'] = vars_data.loc[second_var, 'Value']

    if seed == 4:
        Card = Putchar_card(char_name=var_name)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'

        vars_data.loc[var_name, 'Putchar'] = True

    if seed == 5:
        index_add = randint(0, len(vars_data.index) - 1)
        while (index_add == index_var) or (vars_data.iloc[index_add, 1] == 'POINTER'):
            index_add = randint(0, len(vars_data.index) - 1)
        second_var = vars_data.index[index_add]
        Card = Init_card_another_var(left_name=var_name, right_name=second_var)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        vars_data.loc[var_name, 'Declaration'] = True
        if vars_data.loc[second_var, 'Value'] is not None:
            vars_data.loc[var_name, 'Value'] = vars_data.loc[second_var, 'Value']

    if seed == 6:
        Card = Init_by_pointer(char_name=var_name, pointer_name=p_name)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        if vars_data.loc[p_name, 'Type'] is None:
            vars_data.loc[p_name, 'Type'] = 'POINTER'
        if vars_data.loc[p_name, 'Value'] is not None:
            vars_data.loc[var_name, 'Value'] = vars_data.loc[p_name, 'Value']

    if seed == 7:
        Card = Declaration_p_card(pointer_name=p_name)

        if vars_data.loc[p_name, 'Type'] is None:
            vars_data.loc[p_name, 'Type'] = 'POINTER'
        vars_data.loc[p_name, 'Declaration'] = True

    if seed == 8:
        while vars_data.loc[var_name, 'Type'] is None:
            index_var = randint(0, len(vars_data.index) - 1)
            var_name = vars_data.index[index_var]

        Card = Init_p_card(p_name=p_name, p_ref=var_name)

        if vars_data.loc[p_name, 'Type'] is None:
            vars_data.loc[p_name, 'Type'] = 'POINTER'
        vars_data.loc[p_name, 'Declaration'] = True
        if vars_data.loc[p_name, 'Value'] is not None:
            vars_data.loc[p_name, 'Value'] = vars_data.index[index_p]

    if seed == 9:
        Card = Putchar_p_card(pointer_name=p_name)

        if vars_data.loc[p_name, 'Type'] is None:
            vars_data.loc[p_name, 'Type'] = 'POINTER'

        vars_data.loc[p_name, 'Putchar'] = True

    if seed == 10:
        index_add = randint(0, len(vars_data.index) - 1)
        while (index_add == index_p) or (vars_data.iloc[index_add, 1] == 'VAR'):
            index_add = randint(0, len(vars_data.index) - 1)
        second_p = vars_data.index[index_add]
        Card = Pointer_to_pointer(p_1=p_name, p_2=second_p)

        if vars_data.loc[p_name, 'Type'] is None:
            vars_data.loc[p_name, 'Type'] = 'POINTER'
        if vars_data.loc[second_p, 'Value'] is not None:
            vars_data.loc[p_name, 'Value'] = vars_data.loc[second_p, 'Value']

    if seed == 11:
        Card = Value_from_pointer(char_name=var_name, pointer_name=p_name)

        if vars_data.loc[var_name, 'Type'] is None:
            vars_data.loc[var_name, 'Type'] = 'VAR'
        if vars_data.loc[p_name, 'Type'] is None:
            vars_data.loc[p_name, 'Type'] = 'POINTER'
        if vars_data.loc[p_name, 'Value'] is not None:
            vars_data.loc[var_name, 'Value'] = vars_data.loc[p_name, 'Value']

    if seed == 12:
        index_add = randint(0, len(vars_data.index) - 1)
        while (index_add == index_p) or (vars_data.iloc[index_add, 1] == 'VAR'):
            index_add = randint(0, len(vars_data.index) - 1)
        second_p = vars_data.index[index_add]

        Card = Value_to_value_p(p_1=p_name, p_2=second_p)

        if vars_data.loc[p_name, 'Type'] is None:
            vars_data.loc[p_name, 'Type'] = 'POINTER'
        if vars_data.loc[second_p, 'Type'] is None:
            vars_data.loc[second_p, 'Type'] = 'POINTER'
        if vars_data.loc[second_p, 'Value'] is not None:
            vars_data.loc[p_name, 'Value'] = vars_data.loc[second_p, 'Value']

    return vars_data, Card


# Функция генерации списка карточек на драфте
def analyse_data(vars_data, word, n):
    cards_array = []
    type_of_generation = {'normal': 90, 'random': 10}  # 90% и 10% соотвественно
    for i in range(n):
        if select_type(type_of_generation) == 'normal':
            vars_data, Card = create_card(vars_data, word)
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


# Функция, генерирущая очередной драфт карточек (вызыввается в main.py)
#
#   n -- Количество карточек на драфте
#   vars_data -- DataFrame (pandas) с информацией переменных и указателях
#   word -- слово, которое по заданию надо распечатать игроку
def generate_draft(n, vars_data, word):
    if len(vars_data.index) == 0:
        # Число от балды, возможно стоит придумать, как его вычислять
        vars_amount = 2*len(word) + 2
        vars_data = generate_vars(vars_amount)

    # кортеж с измененнными DataFrame & список карточек (в таком порядке!)
    output_tuple = analyse_data(vars_data, word, n)
    return output_tuple
