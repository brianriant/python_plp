num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(f"First Number Added second number = {num1 + num2}")
elif operation == "-":
    print(f"First Number minus second number = {num1 - num2}")
elif operation == "*":
    print(f"First Number multiplied by the second number = {num1 * num2}")
elif operation == "/":
    print(f"First Number divided by the second number = {num1 / num2}")
else:
    print("Invalid operation")
