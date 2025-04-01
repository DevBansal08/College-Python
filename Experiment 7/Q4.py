# Problem: Ask for age and raise a custom exception for invalid values.

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print(e)
