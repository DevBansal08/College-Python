for num in range(2, 101):  
    is_prime = True  
    for divisor in range(2, num // 2 + 1):  
        if num % divisor == 0:
            is_prime = False  
            break  
    if is_prime:
        print(num, end="  ")
