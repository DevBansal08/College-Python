num = 2
while num <= 100:
    c=1
    divisor = 2
    while divisor <= num // 2:
        if num % divisor == 0:
            c=0 
            break
        divisor += 1
    if c==1:
        print(num, end="  ")
    num += 1  
