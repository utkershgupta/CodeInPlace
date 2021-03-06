# CodeInPlace
This repository contains the final project which I created in CodeInplace program by Stanford University

The WordGuess game

When the user plays WordGuess, the computer first selects a secret word at random from a list built into the program. The program then prints out a row of dashes—one for each letter in the secret word and asks the user to guess a letter. If the user guesses a letter that is in the word, the word is redisplayed with all instances of that letter shown in the correct positions, along with any letters correctly guessed on previous turns. If the letter does not appear in the word, the user is charged with an incorrect guess. The user keeps guessing letters until either (1) the user has correctly guessed all the letters in the word or (2) the user has made eight incorrect guesses.

In order to write the program that plays WordGuess, you should design and test your program in two parts. The first part consists of getting the interactive part of the game working with a fixed set of secret words (that are initially provided for you). The second part consists of replacing the supplied version of the secret word list with one that reads words from a file. The rest of this handout describes these two parts in more detail.


WordGuess Game: Part I—Playing the game
In the first part of this assignment, your job is to write a program that handles the user interaction component of the game. To solve the problem, your program must be able to:
• Choose a random word to use as the secret word. That word is chosen from a word list, as described below. (An initial implementation of this is provided for you.)
• Keep track of the user’s partially guessed word, which begins as a series of dashes and then gets updated as correct letters are guessed.
• Implement the basic control structure and manage the details (ask the user to guess a letter, keep track of the number of guesses remaining, print out the various messages, detect the end of the game, and so forth).
For this part of the assignment, you will simply make use of a function that we’ve given you called get_word that returns a word (string) randomly chosen from a small list of words that will allow you to test your program. The initial code you are provided for the get_word function is only a temporary expedient to make it possible to code this part of the assignment. In Part II, you will reimplement the get_word function we’ve provided with one that reads a list of words from a data file in order to select the random word from a much larger set of possibilities.

WordGuess Game: Part II—Reading a word list from a file
Part II is much easier than Part I and requires less than half a page of code. Your job in this part of the assignment is simply to re-implement the get_word function so that instead of being hard-coded to select from a meager list of three words, it reads a much larger word list from a file and returns a word from that list. The steps involved in this part of the assignment are as follows:
1. Reimplement the get_word function so that it opens the file specified by the constant LEXICON_FILE and reads it line by line.
2. Read the lines from the file into a list.
3. Using that list of words, randomly return any word in the list from the get_word function.

You can feel free to define additional helper functions if you need to, but it's likely that all the code you need to implement this functionality will fit nicely in the get_word function itself. Note that nothing in the rest of the program should have to change in response to this change in the implementation of get_word. Insulating parts of a program from changes in other parts is a fundamental principle of good software design. Thus, in your implementation of the get_word, you should not be changing the parameters of this function.
As a side note, the file Lexicon.txt contains a very large list of words that can used to make the game more challenging to play, and the final version of your program should use that file for input. But to help you test this part of your program, we also provide a much smaller word list in the file TestLexicon.txt. You can feel free to use the TestLexicon.txt file to help you develop/debug your reimplementation of the get_word function, but make sure the final version of your program works properly with the full Lexicon.txt file.
