# enter first number
number1 = float(input("Enter the first number: "))

# enter second number
number2 = float(input("Enter the second number: "))

# enter operator
operation = input("Enter the operator (+, -, *, /): ")

# Perform the operation and display the result
if operation == '+':
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == '-':
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == '*':
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

 