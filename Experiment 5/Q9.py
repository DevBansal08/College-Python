n = int(input("Enter the number of values: "))
count = [0, 0, 0, 0]
print(f"Enter {n} values (each between 0 and 3):")
for _ in range(n):
    value = int(input())
    if 0 <= value <= 3:
        count[value] += 1
    else:
        print("Invalid input! Only numbers between 0 and 3 are allowed.")
for i in range(4):
    print(f"{i} occurred {count[i]} times")
