input_str = input("Enter a string: ")
result_str = ""
i = 0
while i < len(input_str):
    char = input_str[i]
    if char.islower():  
        result_str += char.upper()  
    else:
        result_str += char 
    i += 1
print(result_str)
