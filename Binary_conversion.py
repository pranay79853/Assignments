# Program to convert a decimal number into binary

decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)

print("Binary number is:", binary[2:])