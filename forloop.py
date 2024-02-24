# names=["bharath","hema","lakshmi"]
# for name in names:
#     print(name)
#     if name=="bharath":
#         print(f"HI {name}")
# num=[1,2,3,4,5,6]
# sq=[]
# s=[]
# q=[]
# for i in num:
#     sqr=i**2
#     sqr1=i**3
#     sqr2=i**4
#     sq.append(sqr)
#     s.append(sqr1)
#     q.append(sqr2)
# print(sq)
# print(s)
# print(q)
# name = ["bharath","hema","niharika"]
# name.extend("rajesh")
# print(name)

#calculate average height 
#we shldn't use sum and len function
#use range and split function and use round the overall whole number 
height=input("enter the heights to find the average height ")
height_list=height.split()
count=0
for heights in height_list:
    count+=1
for i in range(count):
    height_list[i]=int(height_list[i])
total=0
for person in height_list:
    total+=person

avg=total/count
print(round(avg))




































































































