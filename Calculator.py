# Calculator

print("Welcome to the Calculator!!!")

calculations=True
f_num=0
n_num=0

f_num=float(input("What's the first number?: "))

# creating a function to perform calculations

def calc(f_num, n_num):
    print("+\n-\n*\n/")
    operation=input("Pick an operation: ")
    n_num=float(input("What's the next number?: "))
    if operation=="+":
        result=f_num+n_num
    elif operation=="-":
        result=f_num-n_num
    elif operation=="*":
        result=f_num*n_num
    elif operation=="/":
        result=f_num/n_num
    print(f"{f_num} {operation} {n_num} = {result}")
    again=input("Type 'y' to continue calculating with or type 'n' to start a new calculation: ")
    if again=="y":
        f_num=result
        calc(f_num, n_num)
    elif again=="n":
        print("\n"*20)
        f_num=float(input("What's the first number?: "))
        calc(f_num, n_num)


while calculations:
    calc(f_num, n_num)



# 2nd method



# def add(a1,a2):
#     return a1+a2   
# def subtract(a1,a2):
#     return a1-a2
# def divide(a1,a2):
#     return a1/a2
# def multiply(a1,a2):
#     return a1*a2

# operations={
#     "+":add,
#     "-":subtract,
#     "*":multiply,
#     "/":divide,
# }
# print("Welcome to the Calculator!!!")

# calculations=True
# f_num=0
# n_num=0

# f_num=float(input("What's the first number?: "))

# # ceating a function for the calculations

# def calc(f_num, n_num):
#     for symbol in operations:
#         print(symbol)
#     operator=input("Pick an operation: ")
#     n_num=float(input("What's the next number?: "))
#     # if operator=="+":
#     #     result=add(f_num, n_num)
#     # elif operator=="-":
#     #     result=subtract(f_num, n_num)
#     # elif operator=="*":
#     #     result=multiply(f_num, n_num)
#     # elif operator=="/":
#     #     result=divide(f_num, n_num)
    
#     result=operations[operator](f_num, n_num)
    
#     print(f"{f_num} {operator} {n_num} = {result}")
#     again=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
#     if again=="y":
#         f_num=result
#     elif again=="n":
#         print("\n"*20)
#         f_num=float(input("What's the first number?: "))
#         calc(f_num, n_num)
        
        
# while calculations:
#     calc(f_num, n_num)