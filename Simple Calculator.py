a = float(input("what is the first number:"))
b = float(input("what is the second number:"))
operation = input("Choose the operation, your options are:'-','+','/','*','%'")
Negative = a-b
add = a+b
divide = a/b
multiply = a*b
percentage = (a/100)*b
if operation == "-":
    print(Negative)
elif operation == "+":
    print(add)
elif operation == "/":
    print(divide)
elif operation == "*":
    print(multiply)
elif operation == "%":
    print(percentage)
else:
    print("operation is invalid")


