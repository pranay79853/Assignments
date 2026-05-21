# Program to check whether the age entered is correct or not
# and also check whether the age is even or odd

age = int(input("Enter your age: "))

# Checking if age is valid
if age <= 0 or age > 120:
    print("Error: Invalid age entered.")
else:
    print("Age entered is correct.")

    # Checking even or odd
    if age % 2 == 0:
        print("The age is Even.")
    else:
        print("The age is Odd.")