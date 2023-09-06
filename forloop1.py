stop=int(input("Enter stop range :"))
start=int(input("Enter start Range :"))
sum=0
for i in range(start,stop+1):
    print(i,end=" ")
    sum=sum+i
print()
print("Sum of series :",sum)
    
