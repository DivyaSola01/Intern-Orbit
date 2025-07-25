# Simple Calculator

# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display operation choices
print("Choose the operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice == '1':
    result = num1 + num2
    operation = '+'
elif choice == '2':
    result = num1 - num2
    operation = '-'
elif choice == '3':
    result = num1 * num2
    operation = '*'
elif choice == '4':
    if num2 == 0:
        result = "Error! Division by zero."
        operation = '/'
    else:
        result = num1 / num2
        operation = '/'
else:
    result = "Invalid operation selected."
    operation = ''

# Display result
if isinstance(result, (int, float)):
    print(f"\nResult: {num1} {operation} {num2} = {result}")
else:
    print(f"\n{result}")
