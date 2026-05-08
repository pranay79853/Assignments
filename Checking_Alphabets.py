# Program to check whether a character is an alphabet or not

ch = input("Enter a character: ")

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print(ch, "is an alphabet.")
else:
    print(ch, "is not an alphabet.")