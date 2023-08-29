ch=input("Enter any character :")
match ch.lower():
    case 'a'|'e'|'o'|'i'|'u':
        print("Vowel")
    case _:
        print("Consonant")
