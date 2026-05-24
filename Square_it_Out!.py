# Program to create square values and separate odd and even squares

# Taking range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Creating list of square values
squares = []

for i in range(start, end + 1):
    squares.append(i ** 2)

print("Square values:", squares)

# Separating odd and even square values
even_squares = []
odd_squares = []

for num in squares:
    if num % 2 == 0:
        even_squares.append(num)
    else:
        odd_squares.append(num)

# Displaying results
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)