WIN = 1
NO_WIN = 0

def check_winner(word, current_state):
    i = 0
    while (i + len(word) - 1 < len(current_state)):
        cut = current_state[i:i + len(word)]
        if (cut == word):
            return WIN
        i += 1
    return NO_WIN
