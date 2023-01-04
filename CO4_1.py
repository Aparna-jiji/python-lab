class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b  
    def get_perimeter(self):
        return 2*(self.l+self.b)
    def get_area(self):
        return self.l*self.b
    def compare(self,c):
        try:
            if obj1.get_area()==obj2.get_area():
                print("Both areas are equal")
            elif obj1.get_area()> obj2.get_area():
                print("Area of rectangle obj1 is greater:")
            else:
                print("Area of rectangle obj1 is lesser:")
        except:
            print("cannot be compared")
   
l1=int(input("Enter the first length Rectangle1:"))
b1=int(input("Enter the first breadth Rectangle1:"))
l2=int(input("Enter the second length Rectangle2:"))
b2=int(input("Enter the second breadth Rectangle2:"))
obj1=rectangle(l1,b1)
obj2=rectangle(l2,b2)
obj1.compare(obj2)


