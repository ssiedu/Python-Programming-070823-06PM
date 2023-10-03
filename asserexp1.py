try:
    num=int(input("Enter any number :"))
    assert num%2==0

except:
    print("Not a valid Number ")

else:
    rec=1/num
    print("reciprocal of number :",rec)
