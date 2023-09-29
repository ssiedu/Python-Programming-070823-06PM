class Base:
    def getRect(self):
        self.l=eval(input("Enter Length :"))
        self.b=eval(input("Enter Breadth :"))


class Parent1(Base):
    def calArea(self):
        self.rarea=self.l*self.b


class Parent2:
    def GetNum(self):
        self.r=eval(input("Enter radius of circle :"))
    def calCArea(self):
        self.carea=3.14*self.r*self.r

class child(Parent1,Parent2):
    def display(self):
        print("Area of Rectangle :",self.rarea)
        print("Area of Circle :",self.carea)



C=child()
C.getRect()
C.calArea()
C.GetNum()
C.calCArea()
C.display()


        
