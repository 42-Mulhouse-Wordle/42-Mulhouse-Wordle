import random
from rich.theme import Theme
from rich.console import Console
# from rich.table import Table
from checker import check_word
from dictionary_handler import fill_wordLib

GUESS_PROMPT = "input: "
TITLE = ":writing_hand: :brain: :bulb: [info]Wordle[/] :bulb: :brain: :writing_hand:\n"

def init_console():
	custom_theme = Theme(
	    {"info": "cyan", "placed": "bold bright_green", "correct": "bold bright_yellow", "wrong": "bright_black"}
	)
	console = Console(theme=custom_theme)
	console.clear()
	console.rule(TITLE)
	return console

# table = Table()
# table.add_column("Word", style="wrong", justify="center")
# table.add_row()

# console.print(table)
# console.print("This is an info message", style="info")
# console.print("This is a placed message", style="placed")
# console.print("This is a correct message", style="correct")
# console.print("This is a wrong message", style="wrong")

def run_game(word, word_lib):
	while word_lib.guessing and word_lib.tries_left > 0:
		guess = input(GUESS_PROMPT)
		word_lib = check_word(word, guess, word_lib)
	if word_lib.tries_left == 0:
		print("You lost, the word was: " + word.upper())

def main():
	word_lib = fill_wordLib()
	if word_lib:
		word = random.choice(word_lib.words)
		init_console()
		run_game(word, word_lib)

main()
