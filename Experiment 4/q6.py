num = int(input("Enter a number to find the sum of its digits: "))
total = 0
while num > 0:
    digit = num % 10
    total += digit    
    num //= 10       
print(f"The sum of digits is {total}")