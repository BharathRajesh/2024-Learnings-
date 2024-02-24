#paint can calculation 
import math
def cans(height, weight, coverage):
    area=height*weight
    no_of_cans=math.ceil(area/coverage)
    print(f"{no_of_cans}")

#coverage is equal to no.of sqft can painted in once can
h=int(input("enter the height:"))
w=int(input("enter the weight"))
cover=7
cans(height=h,weight=w,coverage=cover)
