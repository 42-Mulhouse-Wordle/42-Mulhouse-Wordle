def is_valid_length(guess):
	if len(guess) != 5:
		print("Please enter a strict 5 letter's word.")
		return False
	return True

def is_exist(guess, word_lib):
	if guess not in word_lib:
		print("This word doesn't exist in the dictionary.")
		return False
	return True

def check_word(word, guess, nb_try, word_lib):
	if not is_valid_length(guess) or not is_exist(guess, word_lib):
		return False
	


