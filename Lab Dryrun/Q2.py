# WAP to check whether a given list in non monotonic
lst = [1,4,2,3,5]
incr = True
decr = True
for i in range(1 , len(lst)):
    if lst[i] > lst[i - 1]:
        decr = False
    elif lst[i] < lst[i - 1]:
        incr = False
if not (incr or decr):
    print("Non Monotonic")
else:
    print("Monotonic")