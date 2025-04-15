import random
from checker import check_word
from dictionary_handler import fill_wordLib

GUESS_PROMPT = "input: "

def run_game(word, word_lib):
	while word_lib.guessing and word_lib.tries_left > 0:
		guess = input(GUESS_PROMPT)
		word_lib = check_word(word, guess, word_lib)

def main():
	word_lib = fill_wordLib()
	word = random.choice(word_lib.words)
	word = "beats"
	run_game(word, word_lib)
	print(word)

main()
