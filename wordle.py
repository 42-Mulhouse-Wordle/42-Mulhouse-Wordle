import random
from checker import check_word, is_valid_length
from dictionary_handler import WordLib, fill_wordLib

GUESS_PROMPT = "input: "

def run_game(word, word_lib):
	while word_lib.guessing and word_lib.tries_left > 0:
		guess = input(GUESS_PROMPT)
		word_lib = check_word(word, guess, word_lib)

def main():
	word_lib = fill_wordLib()
	word = random.choice(word_lib.words)
	word = "apple"
	run_game(word, word_lib)

main()
