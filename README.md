# Hangman_game
This project is a simple implementation of the classic Hangman game. The player has to guess letters to complete a hidden word before running out of lives.

# How to Play
1.The program randomly selects a word from a predefined list of words.

2.The player is given a limited number of lives (6 in this case).

3.An underscore (_) is displayed for each letter in the chosen word to represent its position.

4.The player enters a letter as a guess.

5.If the letter is present in the chosen word, all occurrences of that letter in the word are revealed, and the updated word is displayed.

6.If the letter is not in the chosen word, the player loses a life, and the remaining lives are displayed.

7.The game continues until either the player completes the word or runs out of lives.

8.If the player completes the word before running out of lives, they win. Otherwise, they lose.

# Acknowledgements
This project uses the random module in Python.
