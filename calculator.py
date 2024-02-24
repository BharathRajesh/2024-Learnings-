import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

operations_dict={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
}

def calculator():
    num1=float(input("enter the first number:"))
    for symbols in operations_dict:
        print(symbols,end=" ")
    
    countinue_flag=True
    while countinue_flag:
        num2=float(input("enter the second number:"))
        op_symbol=input("enter the symbol of operation you wanna perform:")
        change_fnc=operations_dict[op_symbol]
        output=change_fnc(num1,num2)
        print(output)

        continue_opt=input("enter y to continue the operation and n to start new operation and x to stop the operation: ")
        if continue_opt=="y":
            num1=output
        elif continue_opt=="n":
            countinue_flag=False
            os.system("cls")
            calculator()
        else:
            countinue_flag=False
            print("Bye")
calculator()