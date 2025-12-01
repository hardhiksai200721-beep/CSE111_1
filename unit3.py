print("Functions and Recursion")
# Defining and Calling Function
print("Defining and Calling Function")
def Sample():
    print("HEllO WORLD")
Sample()
# Function with Parameters and Arguments
print("Function with Parameters and Arguments")
def New(name):
    print("Hello "+name)
n=input("Enter your name: ")
New(n)
# Type Conversion and Coercion
print("Type Conversion and Coercion")
a=5.00
b="Hardhik"
c=45
print(int(a))
print(b)
print(float(c)) 
# Math Functions(from math ,module)
print("Math Functions(from math ,module)")
import math
# Square rooot
print("Square root")
a=int(input("Enter a number: "))
print(math.sqrt(a))
# Power
print("Power")
b=int(input("Enter a base: "))
c=int(input("Enter a power: "))
print(math.pow(b,c))
#Ceiling
print("Ceiling")
a=float(input("Enter a number: "))
print(math.ceil(a))
# Floor
print("Floor")
a=float(input("Enter a number: "))
print(math.floor(a))
# Factorial
print("Factorial")
a=int(input("Enter a number: "))
print(math.factorial(a))
#Pi 
print("pi")
print(math.pi)
#Adding New function
print("Adding New function")
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
def add(a,b):
    return a+b
c=add(a,b)
print(c)
# Number is even or odd
print("Even or Odd")
def even_or_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
a=int(input("Enter a number: "))
print(even_or_odd(a))
# Factorial
print("Factorial")
def factorial(a):
    if a==0:
        return 1
    else:
        return factorial(a-1)*a
n=int(input("Enter a number: "))
print(factorial(n))
# Fibonacci Recursive
print("Fibonacci Recursive")
def fibonacci_recursive(a):
    x,y=0,1
    for _ in range(a):
        print(a,end="")
        x,y=y,x+y
n=int(input("Enter a numer: "))
print(fibonacci_recursive(n))
