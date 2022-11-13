num = int(input("Write number"))
for i in range(num,0,-1): #cycle from num to 1 in column
    for j in range(i,0,-1): #cycle from i to 1 in 
        print(j,end = ' ')
    print()