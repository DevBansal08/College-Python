n = int(input("Enter an odd number: "))
mid = n // 2
stars = 1

for i in range(n):
    spaces = abs(mid - i)
    print(" " * spaces + "* " * stars)
    
    if i < mid:
        stars += 1
    else:
        stars -= 1
