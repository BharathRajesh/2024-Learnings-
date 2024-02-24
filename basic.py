'''message="hello world!"
print(message.title())
print(message.upper())
print(message.lower())'''

#day02
#string with a variable
'''first_name="bharath"
last_name="rajesh"
full_name=f"{first_name} {last_name}"
print(full_name.title())
print(full_name.upper())
print(full_name.lower())'''

#information assosiated with a variable
'''first_name="bharath"
last_name="rajesh"
full_name=f"{first_name} {last_name}"
print(f"hello,{full_name.title()}!")'''

#compose entire message and assign to a variable

'''first_name="tom"
last_name="tal"
full_name=f"{first_name} {last_name}"
message=f"hello {full_name.title()}!"
print(message)'''

#adding white space at between

'''print("\tpython")
print("Language:\npython\nc\njava")
print("Language:\n\tPyhton\n\tc\n\tjava")'''

#stripping white spaces after the data

'''fav_lang="  python  "
fav_lang=fav_lang.strip()
#to strip from left side use lstrip() and for right side rstrip() and for both the sides strip()
print(fav_lang)'''

#different case changing technique in string 

'''message="Hello world!"
print(message.capitalize())
print(message.casefold())
print(message.count("o"))
print(message.find("world"))
print(message.index("Hello"))
print(message.isalnum())
print(message.isalpha())
print(message.isascii())
print(message.isdecimal())
print(message.isdigit())
print(message.isidentifier())
print(message.islower())
print(message.isnumeric())
print(message.isprintable())
print(message.swapcase())'''
#numbers
 
 #integers
'''num1,num2 = int(input("enter first number:")),int(input("enter second number: "))
sum,sub,product = num1 + num2,num1 - num2,num1 * num2
#if statement is used to handle to avoid division if second number is zero
if num2 != 0:
    quotient =num1 / num2
    print(f"the {num1} is divide by {num2} the quotient is {quotient}")
else:
    print(f"division is not possible due to second number is {num2} ")

print(f"the sum of 2 numbers are {sum}")

print(f"the subrtation answer is {sub}")

print(f"the multiplication answer is {product}")'''

#indexs and phrases

#5*5 multiplication 
'''for i in range(1,6):
    for j in range(1,6):
        print(i*j, end=' ')
    print()'''
# Initialize a 5x5 array with zeros
'''multiplication_table = [[0 for _ in range(5)] for _ in range(5)]

# Populate the array with the multiplication values
for i in range(1, 6):
    for j in range(1, 6):
        multiplication_table[i-1][j-1] = i * j

# Display the multiplication table
for row in multiplication_table:
    print(row)'''

#5*5 muliplication to display in array using numpy
'''import numpy as np
numbers = np.arrange(1, 6)
print(numbers[:, np.newaxis]*numbers)'''
#print a variable without declaring a variable
'''print(num := 23 )
print(num*23)'''
#averaging the list of values which has different index counts 
'''def average (*nums):
    avg = sum(nums)/len(nums)
    print(int(avg))

average(12,234,443,35)
average(9487,245)
'''
#inserting element into a list in 2 different methods
my_list=[1,2,3,4,5]
my_val=6
#first method
'''my_list.insert(6,my_val)
print(my_list)'''
#second method (slice notation)
'''my_list[6:6] = my_val
print(my_list)'''#not working

#create an random password generator
# import random
# lower ="abcdefghijklmnopqrstuvwxyz"
# upper = lower.upper()
# numbers = '1234567890'
# symbols="!@#$%^&*()"
# all = numbers+lower+upper+symbols
# length = int(input("enter how many numbers do you need?"))
# password =""
# for _ in range(length):
#     password = "".join([password,random.choice(all)])

# print(password)

# def foo(n):
#     if n<=9:
#         return 3
#     return foo(n-3) * foo(n-2)
# print(foo(12)) #27

#write a function to reverse a string
# class node:
#     def __init__(self,data):
#         self.item = data
#         self.next = None
#         self.prev = None

# def reverse(s):
#     headnode = None
#     prevnode = headnode
#     for ch in s:
#         n=node(ch)
#         n.prev=prevnode
#         n.next=None
#         if prevnode:
#             prevnode.next=n
#         prevnode=n
#     result=""
#     while prevnode:
#         result += prevnode.item
#         prevnode = prevnode.prev
#     return result
# print (reverse("Learn 2 code"))

#swapping 2 value in variables
# a=2
# b=3
# temp =a
# a = b
# b = temp
# print(f"{a},{b}")

#exercise 2 adding 2 numbers by gettin input

# first_number=input("enter first number :")
# second_number = input("enter the second number:")
# sum = first_number+second_number
# print(sum)

#exercise 3 

# number = input("enter the numbers to be added:")
# # fst_num=number[0]
# # snd_num=number[1]
# # print(int(fst_num)+int(snd_num))
# total_sum = 0
# for num in number :
#     total_sum += int(num)

# print(f"the giver number sum is {total_sum}")

# print(5+2*3-2+10//5)

#BMI bodomass theorem
# pemdas=int(82/(6**2))
# print(pemdas)

#assignment operator 
#shortend operators 
# a,b = 5,6
# c=a+b
# c += a
# all=a,b,c
# # print(all)
# print(a==5)
# print(a<=5)
# print(a>=5)
# print(a!=5)

#logical operator
#and,or,not
# a,b=5,6
# a=False
# print(a>b and b<a)
# print(a>b or b<a)
# print(not(a))

#bitwise operators
#&(and),|(or),^(xor),~(negation),<<(left shift),>>(right shift)
# a=28
# b=23
# print(a&b)
# a=17
# b=24
# print(a|b)
# print(a^b)
# a=45
# print(~a)
# a=68
# n=2
# print(a<<n)
# a=56
# n=3
# print(a>>n)

#identity operators is isnot
# a=10
# b=10
# print(id(a))
# print(id(b))

#membership operator

#exercise calculate bmi and get the value in int
weight= input("enter the weight:")
height = input("enter the height")
bmi=int(weight/(height**2))
print(bmi)