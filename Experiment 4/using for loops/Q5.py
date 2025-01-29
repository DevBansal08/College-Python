num = int(input("Enter a number to check if it's a palindrome: "))
og = num
reversed_num = 0
num_digits = len(str(num)) 
for _ in range(num_digits):  
    digit = num % 10  
    reversed_num = reversed_num * 10 + digit  
    num //= 10  

if og == reversed_num:
    print(f"{og} is a palindrome.")
else:
    print(f"{og} is not a palindrome.")
