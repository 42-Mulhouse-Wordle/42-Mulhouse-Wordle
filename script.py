import random

class WordLib:
	def __init__(self):
		self.words = []

	def __iter__(self):
		return iter(self.words)

	def add_word(self, word):
		self.words.append(word)

def fill_wordLib():
	word_lib = WordLib()
	with open('words.txt','r') as file:
		for line in file:
			line = line.strip()
			if line:
				word_lib.add_word(line)
	return word_lib

def check_length(guess):
	if len(guess) != 5:
		print("Please enter a strict 5 letter's word.")
		return True
	return False

def check_word(word, guess, nb_try):
	if check_length(guess):
		return False


def run_game(word, word_lib):
	boolean = True
	nb_try = 0
	while boolean and nb_try < 6:
		guess = input("Guess a letter: ")
		if check_word(word, guess, nb_try):
			print("Congratulations! You guessed the word.")
			boolean = False

def main():
	word_lib = fill_wordLib()
	word = random.choice(word_lib.words)
	run_game(word, word_lib)


main()

