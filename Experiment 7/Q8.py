#wap to use else and finally exceptions only

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
except:
    print("An error occurred!")
    
else:
    print(f"Hello {name}, you are {age} years old!")
    
finally:
    print("Thanks for using the program!")