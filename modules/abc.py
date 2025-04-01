class Calculator:
    def calculate(self):
        print("Menu:")
        print("+ for addition")
        print("- for subtraction")
        print("* for multiplication")
        print("/ for division")
        
        operation = input("Enter operation: ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Cannot divide by zero!"
            result = num1 / num2
        else:
            return "Invalid operation!"
            
        return result

calc = Calculator()
print(calc.calculate())