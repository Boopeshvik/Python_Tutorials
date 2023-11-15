import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses some words from the list
    while '-' in word or '' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed

    lives = 7

while len(word_letters) > 0 and lives > 0:
    print('you have',lives,'lives left and you have used these letters:',''.join(used_letters))
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print ('current word:',''.join(word_list))

    user_letter = input("Guess the letter:").upper()
    if user_letter in alphabet - used_letters:
        used_letter.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print('')

        else:
            lives = lives-1
            print('\nYour letter,', user_letter, 'is not in the word.')


    elif user_letter in used_letters:
        print('\nYou have already used that letter. Guess another letter.')

    else:
        print('\nThat is not a valid letter.')

if lives == 0:
    print('You died, sorry. The word was', word)
else:
    print('YAY! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()


