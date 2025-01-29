l=[]

for i in range(1000,2001):
    power_sum=0
    leng=len(str(i))
    x = i % 10
    power_sum += x**leng
    i //= 10

    for j in range(leng):
        if power_sum == i:
            l.append(power_sum)
print(l)
    
        #1000 se 2000 tk
