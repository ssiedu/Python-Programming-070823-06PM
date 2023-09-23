num=int(input("Enter any number :"))
temp=num
rev=0
tod=0
sod=0
while num!=0:#1234  123  12 1
    rev=rev*10+num%10
    sod=sod+num%10
    tod=tod+1
    num=num//10


print("Reverse Number :",rev)
print("Total number of digit :",tod)
print("Sum of digits :",sod)
if temp==rev:
    print("pallindrome")
else:
    print("Not pallindrome")





'''rev=0*10+1234%10
rev=0+4  = 4
num=1234//10
num=123


rev=4*10+123%10
rev=40+3
rev =43
num=123//10 = 12

rev = 43*10+12%10
rev = 430+2
rev = 432
num=12//10  = 1

rev = 432*10+1%10
rev  = 4320+1
rev = 4321

num=1//10  = 0'''


