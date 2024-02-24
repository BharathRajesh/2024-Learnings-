# count=1
# while count<=1000:
#     print(count)
#     count+=1
#     if count==60:
#         print("false")
# else:
#     print("exited loop")
# print("loop done")
total=0
number=int(input("please enter a number: "))
while number>=0:
    total+=number
    number=int(input("please enter a number: "))
    print(total)
    if total==20:
        break
    elif number<=-1:
        break
    elif number<=0:
        break
print("out of loop")