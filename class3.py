class Area:
    def getdata(self):
        self.r=eval(input("Enter radius of circle :"))
    def calArea(self):
        self.area=3.14*self.r*self.r
    def display(self):
        print("Area of circle :",self.area)

A=Area()
A.getdata()
A.calArea()
A.display()
