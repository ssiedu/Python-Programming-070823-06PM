try:
    a=int(input("Enter the value of a :"))
    b=int(input("Enter the value of b :"))
    c=a/b
    print("value of c :",c)

except ZeroDivisionError:
    print("Divide By Zero Not Allowed")
except:
    print("Some Error Occured")

'''except ValueError:
    print("Value Mismatch")'''
