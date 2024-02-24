# def greet(name,dept):
#     print(f"hi {name}")
#     print(f"are you at {dept} department")

# greet("bharath","cs")
# def multiply(*numbers):
#     c=1
#     for i in numbers:
#         c*=i
#     print(c)
# multiply(1,2,3,4,5,6,7)
def division(*numbers):
    result=numbers[0]
    for num in numbers[1:]:
        if num!=0:
            result/=num
            print(result)
        else:
            print("the enteres numbers has zero")

division(1,2,3,4,5)