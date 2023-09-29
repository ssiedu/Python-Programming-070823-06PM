from multipledispatch import dispatch

@dispatch(int,int)
def product(fnum,snum):
    result=fnum*snum
    print("product of two int value :",result)


@dispatch(float,float)
def product(fnum,snum):
    result=fnum*snum
    print("product of two float values :",result)

@dispatch(int,int,int)
def product(fnum,snum,tnum):
    result=fnum*snum*tnum
    print("product of three int values :",result)

@dispatch(int,float)
def product(fnum,snum):
    result=fnum*snum
    print("product of two diff value :",result)



product(10,20)
product(11,22)
product(2,2.2)
product(2,3,4)
product(12.3,3.4)



    
