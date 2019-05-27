from check_win import check_winner
from cards import output_string

def interpretation(stack_1, stack_2, word, winner):
    try:
        for num in range(len(stack_1)):
            stack_1[num].action()
            if (check_win(word, output_string)):
                winner = 1
                return 1
            stack_2[num].action()
            if (check_win(word, output_string)):
                winner = 2
                return 1
    except RuntimeError as err:
        print(err)
    return 0
