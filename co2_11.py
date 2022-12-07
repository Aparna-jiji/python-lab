l=int(input("enter lenghth of rectangle: "))
b=int(input("enter breadth of rectangle: "))
h=int(input("enter height of triangle: "))
arr=lambda x,y:x*y
arsq=lambda x:x*x
art=lambda x,y:0.5*x*y
print("area of rectangle: ",arr(l,b))
print("area of square: ",arsq(l))
print("area of triangle: ",art(b,h))
