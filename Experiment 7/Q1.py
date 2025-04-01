# Q1)Get a list from the user, ask for an index, and handle IndexError and ValueError.Problem: Keep asking for an integer until the user enters a valid one.


size = int(input("How many numbers do you want to enter? "))
numbers=[]
for i in range(size):
    numbers.append(int(input(f"Enter number : ")))

print("Your list is:", numbers)
while True:
    try:
        pos = input("Enter position to access: ")
        pos = int(pos)
        print(numbers[pos])
        break
    except:
        print("Enter a valid index")