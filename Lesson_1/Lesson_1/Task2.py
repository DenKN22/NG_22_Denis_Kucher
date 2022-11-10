import math
operation =  input("Write you operation (+,-,/,*,sqr,sqrt): ")
print("if you choose sqr or sqrt write only first a")
a = int(input("Write a: "))
b = int(input("Write b: "))

if operation == '+':
    print("You answer ",a+b)
if operation == '-':
    print("You answer ",a-b)
if operation == '/':
    print("You answer ",a/b)
if operation == '*':
    print("You answer ",a*b)
if operation == 'sqr':
    print("You answer ",a**2)
if operation == 'sqrt':
    print("You answer ",math.sqrt(a))
