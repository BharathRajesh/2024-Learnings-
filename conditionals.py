#if statement with pass example with nested loop
x,y=int(input("enter x value:")),int(input("enter y value:"))
if x>10 and y>10:
    if x>20 and y>20:
     print("x value is greater than 20")
     print("y value is greateer than 20")
    else:
       pass
else:
     print("x value is lesser than 10")
     print("y value is lesser than 10")
    
