# Program to swap three numbers

# Taking input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping the numbers
a, b, c = c, a, b

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)