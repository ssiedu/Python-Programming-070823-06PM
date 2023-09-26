class Base1:
    def getBase(self):
        self.base=eval(input("Enter Base of triangle :"))


class Base2:
    def getHeight(self):
        self.Height=eval(input("Enter height of triangle:"))


class Derive(Base1,Base2):
    def calculate(self):
        self.area=0.5*self.base*self.Height
        print("Area of triangle :",self.area)


D=Derive()
D.getBase()
D.getHeight()
D.calculate()
