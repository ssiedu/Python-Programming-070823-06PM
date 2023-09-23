class EvenOdd:
    def getNum(self):
        self.num=int(input("Enter Any Number :"))
    def CheckNum(self):
        if self.num%2==0:
            print("Even Number")
        else:
            print("Odd Number")


EO=EvenOdd()
EO.getNum()
EO.CheckNum()
