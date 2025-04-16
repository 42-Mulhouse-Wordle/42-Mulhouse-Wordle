from rich.theme import Theme
from rich.console import Console

FILENAME = 'words.txt'
OPEN_MODE = 'r'
NB_TRIES = 6
FILE_NOT_FOUND = "Error: The file '{}' was not found."
IO_ERROR = "Error: An IOError occurred. Details: {}"
DIC_CORRUPT_ERROR = "The dictionary file is corrupted: '{}' at line {}"
TITLE = ":writing_hand: :brain: :bulb: [info]Wordle[/] :bulb: :brain: :writing_hand:\n"

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
	guess_index = 0
	letter_index = 0
	correct_indices = []
	for letter in guess:
		if letter in word and letter == word[letter_index]:
			word = word[:letter_index] + word[letter_index + 1:]
			obj.green.append(letter)
			correct_indices.append(guess_index)
			letter_index -= 1
		letter_index += 1
		guess_index += 1
	styled_word_index = 0
	styled_word = []
	for letter in guess:
		if styled_word_index in correct_indices:
			style = "bold bright_green"
		elif letter in word:
			obj.yellow.append(letter)
			style = "bold bright_yellow"
			word = word[:word.find(letter)] + word[word.find(letter) + 1:]
		else:
			obj.grey.append(letter)
			style = "bold bright_black"
		styled_word.append(f"[{style}]{letter.upper()}[/]")
		styled_word_index += 1
	Console().print(" ".join(styled_word), justify="center")
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

def print_screen():
	custom_theme = Theme(
	    {"info": "cyan", "placed": "bold bright_green", "correct": "bold bright_yellow", "wrong": "bright_black"}
	)
	console = Console(theme=custom_theme)
	console.clear()
	console.rule(TITLE)
	for i in range(6):
		console.print("- - - - -", justify="center")
	return console

