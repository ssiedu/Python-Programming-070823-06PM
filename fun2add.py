def Addition():
    n1=eval(input("Enter First Number :"))
    n2=eval(input("Enter Second Number :"))
    add=n1+n2
    print("Sum is :",add)

n=int(input("Enter Limit :"))
for i in range(n):
    Addition()
