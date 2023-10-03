try:
    a=10
    b="2"
    c=a/b
    print("value of c :",c)

except ZeroDivisionError:
    print("Zero Division Error")

except TypeError:
    print("Type Mismatch")
