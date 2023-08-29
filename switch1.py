ch=int(input("Enter any number in between 1-5:"))
match ch:
    case 1:
        print("C programming")
    case 2:
        print("CPP programming")
    case 3:
        print("Python")
    case 4:
        print("Java")
    case 5:
        print("ROR")
    case _:
        print("Invalid choice")
