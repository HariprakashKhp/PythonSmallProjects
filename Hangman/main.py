from matplotlib import lines
from random_word import RandomWords
import string
r = RandomWords()

def get_valid_word():
    word = r.get_random_word()
    while '-' in word or ' ' in word:
        word = r.get_random_word()
    return word.upper()



def hangman():
    word = get_valid_word()
    word_letters = set(word)
    used_letters = set()
    alphabets = set(string.ascii_uppercase)

    lives = 6 

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current Word: ", " ".join(word_list))

        user_letter = input("Guess a letter ").upper()

        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives -= 1
                print(f"The guessed letter '{user_letter}' is not in the word")
        elif user_letter in used_letters:
            print("Letter already used")
        else:
            print("Invalid character. Try again!")
    
    if lives == 0:
        print(f"Sorry you lost the game. The word is {word}")
    else:
        print(f"Yea, you guessed the word, {word}")

hangman()