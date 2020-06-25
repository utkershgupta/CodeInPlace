"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "TestLexicon.txt"    # File to read word list from



def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    secret_word=secret_word.lower()
    word=""
    guessed_words_list=[]
    secret_word_list=[]
    INITIAL_GUESSES = 8  # Initial number of guesses player starts with

    # Create lists for secret word and empty list with same character for guessed word

    for i in secret_word:
        secret_word_list.append(i)
        guessed_words_list.append("")

    # Start a while loop to monitor chances and asking user for input

    while INITIAL_GUESSES<=8:
        print("The word now looks like this: ",end="")
        for char in secret_word:
            if char in word:
                print(char.upper()," ", end="")
            else:
                print("_", " ", end="")
        print()
        print("You have",INITIAL_GUESSES,"left")

        # Asks user to input the letter and then convert it to lower case to normalize
        x=input("Type a single letter here, then press enter: ").lower()

        # compare the length of user input
        if len(x)>1:
            print("Guess should only be a single character.")

        if x.isalpha()==0:
            print("Guess should only be an Alphabet.")
            INITIAL_GUESSES = INITIAL_GUESSES-1

        # Check whether the letter input is in secret word
        elif len(x)==1 and x not in secret_word:
            print("There are no", x.upper(),"'s in the word")
            INITIAL_GUESSES=INITIAL_GUESSES-1

        elif len(x) == 1 and x in secret_word:
            # create a string of guessed alphabets
            word=word+x
            # Make the guessed alphabet at same position in guessed words list as in secret word list position
            for i in range(len(secret_word)):
                if secret_word_list[i]==x:
                    guessed_words_list[i]=secret_word_list[i]

        # Check the number of chances and print Sorry if chances are less than 0

        if INITIAL_GUESSES<=0:
            print("Sorry, you lost. The secret word was:",secret_word.upper())
            break
        if guessed_words_list==secret_word_list:
            print("Congratulations, the word is:",secret_word.upper())
            break






def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  
    """
    file=open(LEXICON_FILE)
    my_list=[]
    for line in file:
        my_list.append(line.strip())
    return random.choice(my_list)



def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
