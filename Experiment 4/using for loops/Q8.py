input_str = input("Enter a string: ")
result_str = ""
for char in input_str:
    if char.islower():  
        result_str += char.upper()  
    else:
        result_str += char 
print(result_str)
