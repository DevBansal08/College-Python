num = int(input("Enter a number to find the sum of its digits: "))
total = 0
num_str = str(num)  
for digit in num_str:
    total += int(digit) 
print("The sum of digits is" ,(total))
