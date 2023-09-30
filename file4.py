file=open("Myfile4.txt","w")
for i in range(3):
    Id=int(input("Enter Id Of Employee :"))
    name=input("Enter Employee Name:")
    sal=eval(input("Enter Employee Salary :"))
    data=str(Id)+"\t"+name+"\t"+str(sal)+"\n"
    file.write(data)

file.close()
    
