FILENAME = 'words.txt'
OPEN_MODE = 'r'
NB_TRIES = 6

class WordLib:
	def __init__(self):
		self.words = []
		self.guessing = True
		self.tries_left = NB_TRIES

	def __iter__(self):
		return iter(self.words)

	def add_word(self, word):
		self.words.append(word)

def fill_wordLib():
	word_lib = WordLib()
	with open(FILENAME, OPEN_MODE) as file:
		for line in file:
			line = line.strip()
			if line:
				word_lib.add_word(line)
	return word_lib
