#playing rock paper scissor
import random
value=input("enter rock 0 and for paper 1 and for scissor 2: ")
man=int(value)
if man>=3 or man<0:
    print("enter a valid number!")
else:
    lst=[0,1,2]
    comp=random.choice(lst)
    print(f"{man} * {comp}")
    if man==comp:
        print("It's a draw")
    elif man==0 and comp==2:
        print("u win!")
    elif man==2 and comp==0:
        print("comp wins")
    elif man<comp:
        print("computer win!")
    elif man>comp:
        print("u win!")
    else:
        print("u have invalid number!")