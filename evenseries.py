start=int(input("Enter start Range :"))
stop=int(input("Enter stop range :"))

sum=0
for i in range(start,stop+1):
    if i%2!=0:
        print(i,end=" ")
        sum=sum+i
print()
print("Sum of series :",sum)
    
