import random
from rich.console import Console
from checker import check_word
from dictionary_handler import fill_wordLib, print_screen

GUESS_PROMPT = "[cyan]input: [/]"
LOSS_MESSAGE = "[cyan]You lost, the word was: [/]"
EOF_CATCH = "\n[bright_red]End of File detected, exiting...[/]\n"
SIGINT_CATCH = "\n[bright_red]SIGINT detected, exiting...\n"

def run_game(word, word_lib):
	while word_lib.guessing and word_lib.tries_left > 0:
		try:
			guess = Console().input(GUESS_PROMPT).strip()
		except EOFError:
			Console().clear()
			Console().print(EOF_CATCH)
			word_lib.tries_left = 0
			break
		print()
		word_lib = check_word(word, guess, word_lib)
	if word_lib.tries_left == 0:
		Console().print(LOSS_MESSAGE + " ".join(word.upper()))

def main():
	word_lib = fill_wordLib()
	try:
		if word_lib:
			word = random.choice(word_lib.words)
			print_screen(len(word_lib.words))
			run_game(word, word_lib)
	except KeyboardInterrupt:
		Console().clear()
		Console().print(SIGINT_CATCH)
		Console().print(LOSS_MESSAGE + " ".join(word.upper()))

main()
