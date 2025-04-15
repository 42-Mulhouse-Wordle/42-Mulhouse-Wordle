import random
from checker import check_word, is_valid_length
from dictionaryHandler import WordLib, fill_wordLib

def run_game(word, word_lib):
	boolean = True
	nb_try = 0
	while boolean and nb_try < 6:
		guess = input("Guess a letter: ")
		if check_word(word, guess, nb_try, word_lib):
			print("Congratulations! You guessed the word.")
			boolean = False

def main():
	word_lib = fill_wordLib()
	word = random.choice(word_lib.words)
	run_game(word, word_lib)


main()

