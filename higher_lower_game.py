import list_with_dictionary
import random
import kooltext
import os 
score=0
def display_details(accounts):
#assign the keys to each variable
#comparsion_1
    name=accounts["name"]
    description=accounts["description"]
    country=accounts["country"]
    return f"{name} a {description} from {country}"

def check_answer(guess,followers_count1,followers_count2):
    if followers_count1<followers_count2:
        if guess==1:
            return False
        else:
            return True
    else:
        followers_count1>followers_count2
        if guess==1:
            return True 
        else:
            return False
        
comparsion_2=random.choice(list_with_dictionary.data)

countinue=True
while countinue:
    #assign the variable from dictionary
    comparsion_1=comparsion_2
    comparsion_2=random.choice(list_with_dictionary.data)
    while comparsion_1==comparsion_2:
            comparsion_2=random.choice(list_with_dictionary.data)

    print(kooltext.h_a_lgame)
    print(display_details(comparsion_1))
    print(kooltext.vs)
    print(display_details(comparsion_2))
    followers_count1=comparsion_1["follower_count"]
    followers_count2=comparsion_2["follower_count"]
    print(followers_count1,followers_count2)
    guess=int(input("how has highest follower type 1 or type 2:"))
    os.system('cls')
    if check_answer(guess,followers_count1,followers_count2):
        
        score+=1
        print(f"Thats correct and your score is{score}")
        countinue=True
    else:
        print(f"Thats wrong your score is {score}")
        countinue=False
        








    