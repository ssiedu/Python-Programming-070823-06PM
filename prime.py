num=int(input("Enter any number :"))
flag=0
for i in range(2,(num//2)+1):
    if num%i==0:
        flag=1
        break;

if flag==0:
    print("prime number")
else:
    print("Not Prime ")
