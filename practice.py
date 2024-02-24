# name = "bharat"
# height = 6.4
# age = 23
# print(f"my name is {name} and my age is {age} and the height  is {height}")

#if_else_if statement
#find out the given number is even number or odd number 
#get the input from user 
#write the if the num % 2 ==0 its even else odd

# while True:
#     try:
#         num=int(input("Enter to check whether the given number is even or odd:"))
#         if(num%2==0):
#             print(f"the {num} is even")
#             if (num>10):
#                 print("the given number is greater than 10")
#             else:
#                 print("the given number is lesser than 10")
#             break
#         else:
#             print(f"the {num} is odd")
#         break
    
#     except ValueError:
#         print("the given number is not valid")
#     print("enter again the value and start")

#coding exercise 5
# wght=input("Enter the weight:")
# height=input("enter the weight")
# BMI=round(int(wght)/float(height)**2,2)
# if BMI<16.0:
#     print(f"underweight{BMI}(severe thinness)")
# elif (BMI<=16.9):
#     print("underweight(Moderate thinness)")
# elif (BMI<=18.4):
#     print("underweight(Mild thinness)")
# elif (BMI<=24.9):
#     print("Normal range")
# elif (BMI<=29.9):
#     print("overweight (Pre-obese)")
# elif (BMI<=34.9):
#     print("obese(class l)")
# elif (BMI<=39.9):
#     print("obese(class ll)")
# else:
#     print("obese(class lll)")

#whether the given number is leap year or not
#first get which year we need to calculate the leap year
#enter the if condition matched and
# print whether the given number is leap year
#else return no the given number is not a leap year

# yr=int(input("Enter which year need to be checked whether the given number is leap year: "))
# #yr1,yr2,yr3,yr4=300,700,1900,2000


# if (yr%4==0):
#     if (yr%100==0):
#         print(f"the {yr} is a leap year")
#     elif(yr%400==0):
#         print(f"the {yr} is a leap year")
#     else:
#         print(f"{yr} is not a leap year")
# else:
#     print(f"{yr}is not a leap year")

#roller coaster ticket confirmation
#get the input in feet and check whether the height is above 3 feet
#above 3 feet can ride check the age is under 12 or abobe 18 or within 12 to 18
#and check whether they required photos and print the total bill
# height=int(input("Enter your height in feet:"))
# bill=0
# if (height>=3):
#     print("can ride!")
#     age=int(input("please enter your age"))
#     if (age<12):
#         bill+=100
#         print("your bill is 100Rs")
#     elif(age<18):
#         bill+=150
#         print("your bill is 150Rs")
#     else:
#         bill+=250
#         print("your bill is 250Rs")
#     pic=input("required pic:say Y/N")
#     if pic=="y" or pic=="Y":
#         bill+=50
       
#     print(f"Your total amount to ride is{bill}")

# else:
#     print("no ride")

#order pizza
#get the order on size small = 100 medium = 200 large = 300
#add some pepper onion small = 30 rest two = 50 
#extra add on all size 20

# print("1.Small pizza = 100 \n2.Medium pizza = 200 \n3.Large pizza = 300")
# pi=int(input("Please enter your choise in number: "))
# bill=0
# if (pi==1):
#     bill+=100
#     print("small pizza!")
#     pe=input("add peopper onion 20rs Y/N: ")
#     if pe=="y"or"Y":
#         bill+=30
#         print(f"the total bill is {bill}")
#         ex=input("Do you need to add extra 20rs Y/N: ")
#         if ex=="y"or"Y":
#             bill+=20
#             print(f"the total bill is {bill}")
#     else:
#         print(f"the total is{bill}")
        
# elif (pi==2):
#     bill+=200
#     print("Medium pizza!")
#     pe=input("add peopper onion 20rs Y/N: ")
#     if pe=="y"or"Y":
#         bill+=50
#         print(f"the total bill is {bill}")
#         ex=input("Do you need to add extra 20rs Y/N: ")
#         if ex=="y"or"Y":
#             bill+=20
#             print(f"the total bill is {bill}")
#     else:
#         print(f"the total is{bill}")
# elif (pi==3):
#     bill+=300
#     print("Large pizza!")
#     pe=input("add peopper onion 20rs Y/N: ")
#     if pe=="y"or"Y":
#         bill+=50
#         print(f"the total bill is {bill}")
#         ex=input("Do you need to add extra 20rs Y/N: ")
#         if ex=="y"or"Y":
#             bill+=20
#             print(f"the total bill is {bill}")
#     else:
#         print(f"the total is{bill}")
# else:
#     print(f"please make a right choice {pi} dosen't exist!")


#love calculator
#get the names and convert into lower case
#check true love count in names by adding count exist in names

na1=input("enter boy name: ")
na2=input("enter girl name: ")
name=na1+na2
na=name.lower()

t,r,u,e=na.count('t'),na.count('r'),na.count('u'),na.count('e')
true=t+r+u+e
 
l,o,v,e=na.count('l'),na.count('o'),na.count('v'),na.count('e')
love=l+o+v+e

score=str(true)+str(love)

print(f"the score is {score}")