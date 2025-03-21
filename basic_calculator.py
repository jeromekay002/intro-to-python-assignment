# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

# 1. Ask the user the 1st number
num1 = float(input("First number: "))

# 2. ask user for the 2nd number
num2 = float(input("Second Number: "))

# 3. ask user for the operator for execution
operator = input("Operator (+, -, *, /): ")

# 4. perform the action based on the operator
# 1st operator + 
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if(num2 == 0):
        print("cannot divide by zero")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid Operator")