import random
from checker import check_word
from dictionary_handler import fill_wordLib

GUESS_PROMPT = "Guess a 5 letters word: "
WIN_MESSAGE = "Congratulations! You guessed the word."

def run_game(word, word_lib):
    boolean = True
    nb_try = 0
    while boolean and nb_try < 6:
        guess = input(GUESS_PROMPT)
        if check_word(word, guess, nb_try, word_lib):
            print(WIN_MESSAGE)
            boolean = False

def main():
    word_lib = fill_wordLib()
    word = random.choice(word_lib.words)
    run_game(word, word_lib)

main()
