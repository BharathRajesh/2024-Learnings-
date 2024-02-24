import random 
import kooltext
easy=10
hard=5
def set_difficult(level):
    if level=="easy":
        return easy
    else:
        return hard
def check_answer(guessed_answer,answer,attempt):
    if guessed_answer<answer:
        print("the guessed answer is too less ")
        return attempt-1
    elif guessed_answer>answer:
        print("the guessed answer is too more ")
        return attempt-1
    else:
        print("you won the game ")

def game():
    print(kooltext.kool)
    print("let me think of a number between 1 to 50")
    answer=random.randint(1,50)
    print(answer)
    level=input("enter the level hard or easy ")
    output=set_difficult(level)
    if output!=easy and output!=hard:
        print("play again")
        return
    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {output}")
        guessed_number=int(input("enter the your guess"))
        output=check_answer(guessed_number,answer,output)
        if output==0:
            print("your out of guess")
            return
        elif guessed_number!=answer:
            print("guess again")
game()