class Add:
    def getdata(self):
        self.n1=eval(input("Enter First Number :"))
        self.n2=eval(input("Enter Second Number :"))
    def calAdd(self):
        self.add=self.n1+self.n2
    def display(self):
        print("Addition is :",self.add)
