class Addition:
    def __init__(self):
        self.n1=eval(input("Enter first number :"))
        self.n2=eval(input("Enter Second number :"))

class Sum(Addition):
    def __init__(self):
        Addition.__init__(self)
        self.Add=self.n1+self.n2
        print("Sum is :",self.Add)


S=Sum()
