#Task 1:
#Create a calculator that accepts two numbers and an operator (+, -, , /,%, //, *).
#Perform the operation and display the result.
##Handle division by zero safely.
# Simple Calculator with Error Handling

# Step 1: Get user input
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /, %, //): ")
num2 = float(input("Enter the second number: "))

# Step 2: Perform operation based on the operator
if operator == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operator == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

elif operator == '%':
    if num2 == 0:
        print("Error: Modulus by zero is not allowed.")
    else:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")

elif operator == '//':
    if num2 == 0:
        print("Error: Floor division by zero is not allowed.")
    else:
        result = num1 // num2
        print(f"Result: {num1} // {num2} = {result}")

else:
    print("Invalid operator! Please use +, -, *, /, %, or //")
