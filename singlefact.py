class Base:
    def Factorial(self):
        self.num=int(input("Enter Any Number :"))
        self.f=1
        self.i=1


class Derive(Base):
    def calculate(self):
        while self.i<=self.num:
            self.f=self.f*self.i
            self.i=self.i+1
        print("Factorial of a number :",self.f)


D=Derive()
D.Factorial()
D.calculate()
