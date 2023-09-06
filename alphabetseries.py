start=ord(input("Enter start character:"))
stop=ord(input("Enter stop range of charcter :"))


for i in range(start,stop+1):
    print(chr(i),end=" ")

print()

while start<=stop:
    print(chr(start),end=" ")
    start=start+1
