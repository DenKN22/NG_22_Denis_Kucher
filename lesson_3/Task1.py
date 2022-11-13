import math
def plus():
    print("You answer ",a+b)
def minus():
    print("You answer ",a-b)
def dil():
    print("You answer ",a/b)
def mn():
    print("You answer ",a*b)
def sqr():
    print("You answer ",a**2)
def sqrt():
    print("You answer ",math.sqrt(a))
operation =  input("Write you operation (+,-,/,*,sqr,sqrt): ")
print("if you choose sqr or sqrt write only first a")
a = int(input("Write a: "))
b = int(input("Write b: "))

if operation == '+':
    plus()
if operation == '-':
    minus()
if operation == '/':
    dil()
if operation == '*':
    mn()
if operation == 'sqr':
    sqr()
if operation == 'sqrt':
    sqrt()
