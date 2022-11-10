import math
print("ax^2+bx+c")
a = int(input("Write a:"))
b = int(input("Write b:"))
c = int(input("TWrite c:"))
D = b**2-4*a*c
if(D < 0):
    print("No x")
elif (D == 0):
    print("Only one x = ", (-b)/(2*a))
elif(D > 0):
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)

