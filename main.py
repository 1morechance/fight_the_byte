from char import*
from pointer_char import*
# В cards лежат два массива char_case и pointer__char_case
# Они хранят состояние всех переменных в любой момент времени
from cards import*
# import randomizer

a = Char()
a.set_name('a')
a.set_value('b')

b = Pointer_Char()
b.set_name('b')
b.set_reference('a')

char_case.append(a)

pointer_char_case.append(b)

print(char_case)

print(pointer_char_case)
 
# array = randomize()
# for card in array:
#     card.action()
