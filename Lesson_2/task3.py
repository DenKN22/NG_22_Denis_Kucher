num = int(input("Write number"))
for horiz in range(num,0,-1): #cycle from num to 1 in column
    for vert in range(horiz,0,-1): #cycle from i to 1 in 
        print(vert,end = ' ')
    print()