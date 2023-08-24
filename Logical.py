n1=int(input("Enter First Number :"))#100
n2=int(input("Enter Second Number :"))#50

print("And :",(n1>n2)and(n1==n2))#False
print("Or  :",(n1!=n2) or (n1<n2))#True
print("not :",not(n1==n2))#True
print("And not:",not((n1>n2) and(n1<=n2)))#True
print("Or not :",not((n1<n2) or (n1!=n2)))#False
print("And or not :",not(((n1>n2) and not(n1)) or (n1>=n2)))#False
