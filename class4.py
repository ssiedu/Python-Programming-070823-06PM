class SI:
    def getdata(self):
        self.__p=eval(input("Enter principle amount :"))
        self.r=eval(input("Enter rate of interest :"))
        self.t=eval(input("Enter time in year :"))
    def calSI(self):
        self.si=(self.__p*self.r*self.t)/100
        self.total=self.si+self.__p
    def display(self):
        print("Simple interest :",self.si)
        print("Total amount :",self.total)

s=SI()
s.getdata()
s.calSI()
s.display()
print("principle amount :",self.__p)
