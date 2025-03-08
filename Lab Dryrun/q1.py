# WAP to find largest element in a list
list=[10,20,30,40,50]
if list:
    largest= list[0]
    for i in list:
        if i>largest:
            largest = i
    print(largest)  
