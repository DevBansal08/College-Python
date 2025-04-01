#wap to handle custom exceptions

class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise AgeError("Age cannot be negative!")
    elif age < 18:
        raise AgeError("You must be 18 or older!")
    else:
        print("Age is valid! Welcome!")

except ValueError:
    print("Please enter a valid number!")
except AgeError as e:
    print("Age Error:", e)
