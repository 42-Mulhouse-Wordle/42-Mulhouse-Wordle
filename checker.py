INVALID_LENGTH_MESSAGE = "Please enter a strict 5 letters word."

def is_valid_length(guess):
    if len(guess) != 5:
        print(INVALID_LENGTH_MESSAGE)
        return False
    return True

def is_exist(guess, word_lib):
    return True

def check_word(word, guess, nb_try, word_lib):
    if not is_valid_length(guess) or not is_exist(guess, word_lib):
        return False
