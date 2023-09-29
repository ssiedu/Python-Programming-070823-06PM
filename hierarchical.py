class Base:
    def __init__(self):
        self.n1=eval(input("Enter First number:"))
        self.n2=eval(input("Enter Second Number:"))

class child1(Base):
    def Addition(self):
        self.add=self.n1+self.n2
        print("Addition is :",self.add)

class child2(Base):
    def Subtraction(self):
        self.sub=self.n1-self.n2
        print("Subtraction is :",self.sub)

class child3(Base):
    def Multiplication(self):
        self.mul=self.n1*self.n2
        print("Multiplication is :",self.mul)



c1=child1()
c1.Addition()
c2=child2()
c2.Subtraction()
c3=child3()
c3.Multiplication()


        
