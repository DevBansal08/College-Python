n = int(input("Enter the number of values: "))
values = tuple(float(input(f"Enter value {i+1}: ")) for i in range(n))
average = sum(values) / n if n > 0 else 0
print(f"The average of the values is: {average}")
