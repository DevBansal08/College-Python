str = "Hello World! This is a Test String."
capital_count = 0
for char in str:
    if char.isupper(): 
        capital_count += 1 
print(f"capital letters in the string: {capital_count}")