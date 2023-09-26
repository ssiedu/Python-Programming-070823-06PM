class Addition:
    def __init__(self,n1=1,n2=2):
        self.num1=n1
        self.num2=n2
    def calAdd(self):
        self.add=self.num1+self.num2
    def display(self):
        print("value of n1 :",self.num1)
        print("value of n2 :",self.num2)
        print("Sum is :",self.add)


A=Addition(10)
A.calAdd()
A.display()
