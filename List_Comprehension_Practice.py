# 1. Create a list of numbers from 1 to 10
numbers = [x for x in range(1, 11)]
print(numbers)

# 2. Create a list of squares
squares = [x**2 for x in range(1, 11)]
print(squares)

# 3. Create a list of even numbers
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# 4. Create a list of odd numbers
odds = [x for x in range(1, 21) if x % 2 != 0]
print(odds)

# 5. Convert names to uppercase
names = ["john", "alice", "bob"]
upper_names = [name.upper() for name in names]
print(upper_names)