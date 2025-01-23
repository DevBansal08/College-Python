num = int(input("Enter Number: "))
og = num
power_sum = 0
length = len(str(num))
while  num >0:
    x =  num % 10
    power_sum += x**length
    num//=10
if power_sum == og:
    print("Armstrong")
else:
    print("Not Armstrong")
