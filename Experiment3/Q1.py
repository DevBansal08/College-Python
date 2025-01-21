num = int(input("Enter a number: "))

if num % 3 == 0:
    if num % 5 == 0:
        print(f"{num} is divisible by both 3 and 5.")
    else:
        print(f"{num} is divisible by 3 but not by 5.")
else:
    if num % 5 == 0:
        print(f"{num} is divisible by 5 but not by 3.")
    else:
        print(f"{num} is not divisible by both 3 and 5.")

