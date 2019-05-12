'''
Randomizer - генератор рандомных карточек
Контролируемый рандом ("подкрученый")

Генерирует N карточек
'''

from random import randint
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
                              'Init': [False for i in range(m)],      # True OR False
                              'Value': [None for i in range(m)],      # <Value> OR None
                              'Putchar': [False for i in range(m)]},  # True OR False
                            index=names_list)
    vars_data.index.name = 'Variables'
    return vars_data


# Проверка: присвоено ли какое-то значение перерменной
def has_value(var):
    if var['Value'] is None:
        return False
    else:
        return True


# TODO
def create_random_value(vars_data, word):
    card =
    return tuple(vars_data, card)


# Генерация очередной карточки
# TODO: описать создание картчоки (ведь для одно случая разные сценарии)
# TODO: добавить строчки, которые изменяют DataFrame
def create_card(vars_data, word):
    var = vars_data.iloc[randint(0, len(vars_data.index) - 1)]

    if var['Init'] && has_value(var) && var['Putchar']:
        vars_data, card = create_random_card(vars_data, word)
    else:
        if not var['Init']:
            card =

        elif not has_value(var):
            card =

        elif not var['Putchar']:
            card =


    return tuple(vars_data, card)


# Функция генерации списка карточек на драфте
def analyse_data(vars_data, word, n):
    cards_array = []
    for i in range(n):
        vars_data, card = create_card(vars_data, word)
        cards_array.append(card)
    return tuple(vars_data, cards_array)


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
#   word -- слово, которое по заданию надо распечатать игрок
def generate_draft(n, vars_data, word):
    if len(vars_data.index) == 0:
        # Число от балды, возможно стоит придумать, как его вычислять
        vars_amount = n - 2
        vars_data = generate_vars(vars_amount)

    # кортеж с измененнными DataFrame & список карточек (в таком порядке!)
    output_tuple = analyse_data(vars_data, word, n)
    return output_tuple







