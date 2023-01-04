class Rectangle:
    def __init__(self):
        self.__l =int(input("enter the length of rectangle: "))
        self.__b=int(input("enter the breadth of rectangle: "))
    def __lt__(self,obj2):
        area1=self.__l*self.__b
        area2=self.__l*obj2.__b
        print("Area of rectangle1 is: ",area1)
        print("Area of rectangle2 is: ",area2)
        return area1<area2
print("Enter the length and breadth of first object: ")
obj1=Rectangle()
print("Enter the length and breadth of second object: ")
obj2=Rectangle()
if obj1<obj2:
    print("Rectangle1 is lesser than Rectangle2")
else:
    print("Rectangle1 is greater than Rectangle2")
    


        
        