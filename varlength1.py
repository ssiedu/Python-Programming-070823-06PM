def data(*x):
    print(x)
    for i in x:
        print(i)
    print(x[0])


data(10,20,30,40)

def Keyword(**x):
    print(x)
    for i,j in x.items():
        print(i,j)
    print(x['x'])


Keyword(x=10,y=20,z=30)
