class Base1:
    def getNum1(self):
        self.Num1=eval(input("Enter First Number :"))


class Base2:
    def getNum2(self):
        self.Num2=eval(input("Enter Second Number :"))
        
class Base3:
    def getNum3(self):
        self.Num3=eval(input("Enter Third Number :"))

        
class Derive(Base1,Base2,Base3):
    def calculate(self):
        self.product=self.Num1*self.Num2*self.Num3
        print("product of three numbers :",self.product)


D=Derive()
D.getNum1()
D.getNum2()
D.getNum3()
D.calculate()
