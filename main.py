from cards import*
from randomizer import generate_draft
from pandas import DataFrame

HAND_SIZE = 8
WIN_BY = 'лещ'

data = DataFrame()
hand = (generate_draft(HAND_SIZE, data, WIN_BY))[1]

for card in hand:
    print(card.view())
try:
    for card in hand:
        card.action()
except RuntimeError as err:
    print(err)
