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


# # TODO
# def create_card(vars_data, word):
#     index_main = randint(0, len(vars_data.index) - 1)
#     var = vars_data.iloc[index_main]
#
#     var_name = var.index
#
#     if
#
#
#     return vars_data, card


# Генерация очередной карточки
# TODO: описать создание картчоки (ведь для одно случая разные сценарии)
# TODO: добавить строчки, которые изменяют DataFrame
def create_random_card(vars_data, word):
    index_main = randint(0, len(vars_data.index) - 1)
    var_name = vars_data.index[index_main]

    class_amount = 4  # Пока не все реализовано
    seed = randint(0, class_amount)

    # Топорно, согласен (beta)
    # Пока без поинтеров
    if seed == 0:
        Card = Init_card(char_name=var_name, char_value=word[randint(0, len(word) - 1)])

    if seed == 1:
        Card = Declaration_card(char_name=var_name)

    if seed == 2:
        Card = Init_declaration_card(char_name=var_name, char_value=word[randint(0, len(word) - 1)])

    if seed == 3:
        index_add = randint(0, len(vars_data.index) - 1)
        while index_add == index_main:
            index_add = randint(0, len(vars_data.index) - 1)
        second_var = vars_data.index[index_add]
        Card = Value_to_value_card(left_name=var_name, right_name=second_var)

    if seed == 4:
        Card = Putchar_card(char_name=var_name)


    # Init_by_pointer нельзя просто случайно генерировать
    # (нужно понимать какие у нас указатели))
    # if seed == :
    #         Card = Init_by_pointer(char_name=var_name)


    # if var['Init'] && has_value(var) && var['Putchar']:
    #     vars_data, card = create_random_card(vars_data, word)
    # else:
    #     if not var['Init']:
    #         card =
    #
    #     elif not has_value(var):
    #         card =
    #
    #     elif not var['Putchar']:
    #         card =

    return vars_data, Card


# Функция генерации списка карточек на драфте
def analyse_data(vars_data, word, n):
    cards_array = []
    for i in range(n):
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
        vars_amount = n - 2
        vars_data = generate_vars(vars_amount)

    # кортеж с измененнными DataFrame & список карточек (в таком порядке!)
    output_tuple = analyse_data(vars_data, word, n)
    return output_tuple
