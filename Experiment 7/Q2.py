# Problem: Take two numbers as input, perform division, and handle ZeroDivisionError and ValueError.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print(result)
    
except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")