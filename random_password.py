import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'x', 'Y', 'Z']
numbers = ['0', '1', '2', '3' , '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']
n_letters=int(input("enter how any letters need"))
n_numbers=int(input("enter how many numbers u need"))
n_symbols=int(input("enter how many symbols u need"))
password=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_numbers+1):
    num=random.choice(numbers)
    password+=num
for i in range(1,n_symbols+1):
    sym=random.choice(symbols)
    password+=sym
random.shuffle(password)
shufpass=""
for i in password:
    shufpass+=i
print(shufpass)