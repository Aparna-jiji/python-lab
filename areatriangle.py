#program to find aea of triangle
h=int(input("enter the height of triangle: "))
b=int(input("enter the base of triangle: "))
print("Area is: ",0.5*b*h)

#program to find the area of triangle whoose three sides are given
import math
a=int(input("enter the first side of triangle: "))
b=int(input("enter the second side of triangle: "))
c=int(input("enter the third side of triangle: "))
side=(a+b+c)/2
print("area is : ",math.sqrt(side*(side-a)*(side-b)*(side-c)))

#to find the area of equilateral triangle
s=int(input("enter the side of equilateral triangle: "))
print("area of equilateral triangle is : ",math.sqrt(3/2)*(s**2))
