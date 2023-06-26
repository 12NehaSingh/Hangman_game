import words
import random

# Taking the list of words from file words
chosen_word = random.choice(words.word_list)

#No. of chance
live = 6

#create a tupple to store underscore to show how many no. of letter are there in chosen word
display = []

length = len(chosen_word)
for i in range(0, length) :
    display+= '_'

print(display)

game_over = False

#when the chance is over then loop will  stop
while not game_over :
    guessed_letter = input("Enter the letter:")
    for p in range(len(chosen_word)) :
        if guessed_letter == chosen_word[p] :
            display[p] = guessed_letter
            print("letter match")
            print(display)
    if guessed_letter not in chosen_word :
        live=live-1
        print("wrong guess")
        print(f"Now,you have only  {live} life remain ")

        if live == 0:
            game_over = True
            print("you lose")
    if '_'  not in display :
        print("you win")
        game_over = True







