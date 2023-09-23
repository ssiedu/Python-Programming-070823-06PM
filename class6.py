class Factorial:
    def getNum(self):
        self.num=int(input("Enter Any Number :"))
    def calFact(self):
        f=1
        i=1
        while i<=self.num:
            f=f*i
            i=i+1
        print("Factorial of a number :",f)


F=Factorial()
F.getNum()
F.calFact()
