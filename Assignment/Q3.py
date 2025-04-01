num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (&, |, ^, <<, >>): ")

if operator == '&':
    print(f"Result: {num1 & num2}")
elif operator == '|':
    print(f"Result: {num1 | num2}")
elif operator == '^':
    print(f"Result: {num1 ^ num2}")
elif operator == '<<':
    print(f"Result: {num1 << num2}")
elif operator == '>>':
    print(f"Result: {num1 >> num2}")
else:
    print("Invalid operator!")
