import random
import words
import hangman_stages
life=6
word_guess=random.choice(words.word)
blank=[]
for i in range(len(word_guess)):
    blank+="_"
game_over=False
while not game_over:
    letter_guess=input("guess a letter:").lower()
    for position in range(len(word_guess)):
        letter=word_guess[position]
        if letter==letter_guess:
            blank[position]=letter_guess
    print(blank)
    if letter_guess not in word_guess:
        life-=1
        if life==0:
            game_over=True
            print("you loose")
    if "_" not in blank:
        game_over=True
        print("you win")
    print(hangman_stages.stages[life])