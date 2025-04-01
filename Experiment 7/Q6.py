#wap to handle multiple exceptions
try:
    my_list = [1, 2, 3]
    index = int(input("Enter index to access list: "))
    print("Value at index:", my_list[index])

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"Division result: {result}")

except IndexError:
    print("Error: Index is out of range!")
    
except ValueError:
    print("Error: Please enter valid numbers!")
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    
