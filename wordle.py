import random
from checker import check_word
from dictionary_handler import fill_wordLib, print_screen

GUESS_PROMPT = "input: "
LOSS_MESSAGE = "You lost, the word was: "
EOF_CATCH = "End of File detected, exiting...\n"
NEW_LINE = "\n"
SIGINT_CATCH = "\nSIGINT detected, exiting...\n"

def run_game(word, word_lib):
	while word_lib.guessing and word_lib.tries_left > 0:
		try:
			guess = input(GUESS_PROMPT)
		except EOFError:
			print(EOF_CATCH)
			word_lib.tries_left = 0
			break
		print(NEW_LINE)
		word_lib = check_word(word, guess, word_lib)
	if word_lib.tries_left == 0:
		print(LOSS_MESSAGE + word.upper())

def main():
	word_lib = fill_wordLib()
	try:
		if word_lib:
			word = random.choice(word_lib.words)
			print_screen()
			run_game(word, word_lib)
	except KeyboardInterrupt:
		print(SIGINT_CATCH)
		print(LOSS_MESSAGE + word.upper())

main()
