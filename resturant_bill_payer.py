#get names in input
#split the names and store in list
#and use choise function in random to generate who is gonna pay the bill
import random
names=input("enter the names who all are present:")
list_of_names=names.split()
payer=random.choice(list_of_names)
print(f"{payer} will pay the bill")