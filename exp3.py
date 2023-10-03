try:
    print("Try Block")
    a=int(input("Enter the value of a :"))
    b=int(input("Enter the value of b :"))
    c=a/b

except:
    print("Except Block")
    print("Some Error Occured")
else:
    print("Else Block")
    print("value of c :",c)

finally:
    print("finally Block")
    print("Program Successully Executed")


print("Out of Try and except Block")
