while True:
    uc=input('''Do you want to continue?
1.Yes('y')
2.No('n')
''')
    if uc.lower()=='y' or uc=='1':

        print('''Select Any One :-
1.Addition
2.Subtraction
3.MUltiplication
4.Division
5.Modulus''')
        ch=input("Enter Your choice :")
        num1=eval(input("Enter First Number :"))
        num2=eval(input("Enter Second Number :"))
        match ch:
            case '+':
                print("{} + {} ={}".format(num1,num2,num1+num2))
            case '-':
                print("{} - {} ={}".format(num1,num2,num1-num2))
            case '*':
                print("{} * {} ={}".format(num1,num2,num1*num2))
            case '/':
                print("{} / {} ={}".format(num1,num2,num1/num2))
            case '%':
                print("{} % {} ={}".format(num1,num2,num1%num2))
            case _:
                print("Please Enter Valid choice")
    else:
        break;
