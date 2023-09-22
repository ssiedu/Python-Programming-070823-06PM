class Addition:
    def getdata(self):
        self.num1=int(input("Enter first number :"))
        self.num2=int(input("Enter Second Number :"))
    def calAdd(self):
        self.add=self.num1+self.num2
    def display(self):
        print("Addition is :",self.add)


A=Addition()
A.getdata()
A.calAdd()
A.display()
B=Addition()
B.getdata()
B.calAdd()
B.display()
