class Base:
    def getdata(self):
        self.r=eval(input("Enter radius of circle:"))


class Derive(Base):
    def calArea(self):
        self.area=3.14*self.r*self.r
        print("Area of circle :",self.area)



D=Derive()
D.getdata()
D.calArea()
