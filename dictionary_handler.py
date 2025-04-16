FILENAME = 'words.txt'
OPEN_MODE = 'r'
NB_TRIES = 6

class WordLib:
	def __init__(self):
		self.words = []
		self.previous_guesses = []
		self.guessing = True
		self.tries_left = NB_TRIES
		self.yellow = []
		self.green = []
		self.grey = []

	def __iter__(self):
		return iter(self.words)

	def add_guess(self, guess):
		self.previous_guesses.append(guess)

	def get_previous_guesses(self, word):
		for guess in self.previous_guesses:
			self = print_word(guess, word, self)
		print()
		for lettre in range(ord('a'), ord('z') + 1):
			if chr(lettre) in self.green:
				print('\033[92m' + chr(lettre).upper() + '\033[0m', end=' ')
			elif chr(lettre) in self.yellow:
				print('\033[93m' + chr(lettre).upper() + '\033[0m', end=' ')
			elif chr(lettre) in self.grey:
				print('\033[90m' + chr(lettre).upper() + '\033[0m', end=' ')
			else:
				print(chr(lettre).upper(), end=' ')
		print()

	def add_word(self, word):
		self.words.append(word)

def print_word(guess, word, obj):
	i = 0
	l = 0
	k = []
	for char in guess:
		if char in word and char == word[l]:
			word = word[:l] + word[l + 1:]
			obj.green.append(char)
			k.append(i)
			l -= 1
		l += 1
		i += 1
	i = 0
	for char in guess:
		if i in k:
			print('\033[92m' + char.upper() + '\033[0m', end=' ')
		elif char in word:
			obj.yellow.append(char)
			print('\033[93m' + char.upper() + '\033[0m', end=' ')
			word = word[:word.find(char)] + word[word.find(char) + 1:]
		else:
			obj.grey.append(char)
			print('\033[90m' + char.upper() + '\033[0m', end=' ')
		i += 1
	print()
	return obj

def fill_wordLib():
	word_lib = WordLib()
	with open(FILENAME, OPEN_MODE) as file:
		for line in file:
			line = line.strip()
			if line:
				word_lib.add_word(line)
	return word_lib
