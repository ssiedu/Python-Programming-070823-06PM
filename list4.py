l1=[]
l2=[]
n=int(input("Enter any number :"))
for i in range(1,n+1):
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)

print("Even Series List :")
print(l1)
print("Odd Series List :")
print(l2)
