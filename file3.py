file=open("Myfile3.txt","a")
n=int(input("How many students name do u want to Enter :"))
for i in range(n):
    name=input("Enter Name of Student :")
    file.write(name+"\n")

file.close()
