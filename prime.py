# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num % i ==0:
#             return False
#         return True
# def prime_range(start, end):
#     print(f"the number starts in range {start} and ends at {end}")
#     for num in range(start, end+1):
#         if is_prime(num):
#             print(num)
        
# starting=int(input("enter the start number:"))
# ending=int(input("enter the ending number "))
# prime_range(starting,ending)
#_____________________________________________________________________________
# Program to check if a number is prime or not

#num = 29

# To take input from the user
# num = int(input("Enter a number: "))

# # define a flag variable
# flag = False

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

#     # check if flag is True
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")

# #_____________________________________________________________________________
# num = 407

# # To take input from the user
# #num = int(input("Enter a number: "))

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")
       
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")

import math
def check_prime(num):
    if num==1:
        return False
    for i in range(2,math.ceil(num/2)+1):
        if num%i==0:
            return False
        return True
def prime_range(start,stop):
    for i in range(start,stop+1):
        if check_prime(i):
            print(i)
n=int(input("Enter the number to check prime number: "))
d=int(input("Enter the number to check prime number: "))

prime_range(n,d)