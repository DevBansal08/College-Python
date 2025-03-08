n = int(input("Enter the number of fruits for each set: "))
s1 = []
s2 = []

print("Enter fruits for set s1:")
for i in range(n):
    fruit = input(f"Enter fruit {i+1}: ")
    s1.append(fruit)

print("Enter fruits for set s2:")
for i in range(n):
    fruit = input(f"Enter fruit {i+1}: ")
    s2.append(fruit)

common_fruits = []
for fruit in s1:
    if fruit in s2 and fruit not in common_fruits:
        common_fruits.append(fruit)
print("\nFruits in both sets s1 and s2:", common_fruits)

unique_to_s1 = []
for fruit in s1:
    if fruit not in s2 and fruit not in unique_to_s1:
        unique_to_s1.append(fruit)
print("Fruits only in s1 but not in s2:", unique_to_s1)

all_fruits = []
for fruit in s1 + s2: 
    if fruit not in all_fruits:
        all_fruits.append(fruit)
count_all_fruits = len(all_fruits)
print("Count of all fruits from s1 and s2:", count_all_fruits)