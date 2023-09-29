class Base:
    def __init__(self):
        self.l=eval(input("Enter Length of rectangle :"))
        self.b=eval(input("Enter breadth of rectangle :"))


class Parent(Base):
    def calculateArea(self):
        self.area=self.l*self.b


class child(Parent):
    def display(self):
        print("Area of rectangle :",self.area)


C=child()
#C.getdata()
C.calculateArea()
C.display()
