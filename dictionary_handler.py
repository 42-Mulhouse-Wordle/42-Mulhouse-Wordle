FILENAME = 'words.txt'
OPEN_MODE = 'r'

class WordLib:
	def __init__(self):
		self.words = []

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
