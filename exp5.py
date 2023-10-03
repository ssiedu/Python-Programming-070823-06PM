try:
    age=int(input("Enter Age of Person : "))
    if age<18:
        raise ValueError
except ValueError:
    print("Not eligible for vote")

else:
    print("Eligible for vote")
