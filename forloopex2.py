#find a maximum numbers from list
#include not included
#input  max
#split  len
#range  
numbers=input("enter the numbers to find out maxnum:")
num_list=numbers.split()
count=0
for i in num_list:
    count+=1
for j in range(count):
    num_list[j]=int(num_list[j])
maximum_num=num_list[0]
for num in num_list:
    if num > maximum_num:
        maximum_num=num
print(f"{maximum_num}")
