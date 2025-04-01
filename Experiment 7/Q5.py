#write a program to handle division by zero error

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(result)
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers!")
