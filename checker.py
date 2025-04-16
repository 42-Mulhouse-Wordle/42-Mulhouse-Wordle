from rich.console import Console
from dictionary_handler import NB_TRIES

INVALID_LENGTH_MESSAGE = "[bright_red]Please enter a strict 5 letters word.[/]"
WORD_DOESNT_EXIST = "[bright_red]This word doesn't exist in the dictionary.[/]"
WIN_MESSAGE = "[bright_green]Congratulations you found the word [/][white]{}[/][bright_green] in [/][white]{}[/][bright_green] guesses[/]"
NB_TRIES_DISPLAYED = NB_TRIES + 1

def is_valid_length(guess):
    if len(guess) != 5:
        Console().print(INVALID_LENGTH_MESSAGE)
        return False
    return True

def is_exist(guess, word_lib):
	if guess not in word_lib:
		Console().print(WORD_DOESNT_EXIST)
		return False
	return True

def is_matching(word, guess, word_lib):
	if word == guess:
		Console().print(WIN_MESSAGE.format(" ".join(word.upper()), -word_lib.tries_left + NB_TRIES_DISPLAYED))
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
