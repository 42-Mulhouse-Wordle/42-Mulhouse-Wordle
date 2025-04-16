from rich.console import Console
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 08f1125 (Feature: Add justifed alphabet)
=======

>>>>>>> 3d7adcf (Chore: clean constants in code)
FILENAME = 'words.txt'
OPEN_MODE = 'r'
NB_TRIES = 6
FILE_NOT_FOUND = "Error: The file '{}' was not found."
IO_ERROR = "Error: An IOError occurred. Details: {}"
DIC_CORRUPT_ERROR = "The dictionary file is corrupted: '{}' at line {}"

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
		styled_alphabet = []
		for letter in range(ord('a'), ord('z') + 1):
<<<<<<< HEAD
<<<<<<< HEAD
=======
			style = ""
>>>>>>> 08f1125 (Feature: Add justifed alphabet)
=======
>>>>>>> 3d7adcf (Chore: clean constants in code)
			if chr(letter) in self.green:
				style = "bold bright_green"
			elif chr(letter) in self.yellow:
				style = "bold bright_yellow"
			elif chr(letter) in self.grey:
				style = "bold bright_black"
			else:
				style = "normal"
			styled_alphabet.append(f"[{style}]{chr(letter).upper()}[/]")
		Console().print(" ".join(styled_alphabet), justify="center")

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
    try:
        with open(FILENAME, OPEN_MODE) as file:
            i = 0
            for line in file:
                i += 1
                line = line.strip()
                if line and len(line) == 5 and line.isalpha():
                    word_lib.add_word(line)
                else:
                    print(DIC_CORRUPT_ERROR.format(line, i))
                    return None
    except FileNotFoundError:
        print(FILE_NOT_FOUND.format(FILENAME))
        return None
    except IOError as e:
        print(IO_ERROR.format(e))
        return None
    return word_lib
