alpha=input("Enter any character :")
if alpha>='a' and alpha<='z':
    print("Lower case letter")
elif alpha>='A' and alpha<='Z':
    print("Upper case letter")
elif alpha>='0' and alpha<='9':
    print("Digit")
else:
    print("Special Symbol")
