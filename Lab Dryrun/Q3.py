# WAP to multiply 2 lists
l1 = [1,2,3,4,5]
l2= [6,7,8,9,10]
l3 = []
if len(l1) == len(l2):
    for i in range (len(l1)):
        result = (l1[i]*l2[i])
        l3.append(result)
    print(l3)