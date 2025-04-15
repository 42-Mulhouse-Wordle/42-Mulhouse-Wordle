from dictionary_handler import NB_TRIES

INVALID_LENGTH_MESSAGE = "Please enter a strict 5 letters word."
WORD_DOESNT_EXIST = "This word doesn't exist in the dictionary."
WIN_MESSAGE = "Congratulations you found the word {} in {} guesses"
NB_TRIES_DISPLAYED = NB_TRIES + 1

def is_valid_length(guess):
    if len(guess) != 5:
        print(INVALID_LENGTH_MESSAGE)
        return False
    return True

def is_exist(guess, word_lib):
	if guess not in word_lib:
		print(WORD_DOESNT_EXIST)
		return False
	return True

def is_matching(word, guess, word_lib):
	if word == guess:
		print(WIN_MESSAGE.format(word.upper(), -word_lib.tries_left + 7))
		return True
	return False

def check_word(word, guess, word_lib):
	guess = guess.lower()
	if not is_valid_length(guess) or not is_exist(guess, word_lib):
		return word_lib
	word_lib.add_guess(guess)
	word_lib.get_previous_guesses(word)
	if is_matching(word, guess, word_lib):
		word_lib.guessing = False
		return word_lib
	else:
		word_lib.tries_left -= 1
		return word_lib
