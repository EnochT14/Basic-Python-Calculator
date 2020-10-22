#Written By: @Encobb1

first_number = float(input("What is the first number?:"))
second_number = float(input("What is the second number?:"))
operation = input("what is the operation in lower case letters?")

def calculator(a,b):
    if operation == "division":
        print(a/b)
    elif operation == "addition":
        print(a+b)
    elif operation == "multiplication":
        print(a*b)
    elif operation == "subtraction":
        print(a-b)   
     
    return calculator

print(calculator(first_number, second_number))   