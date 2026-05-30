num = int(input("Enter a number: "))

odd_numbers = [i for i in range(num) if i % 2 != 0]
even_numbers = [i for i in range(num) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

fruits = ["apple", "banana", "mango", "orange", "grapes"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original List:", fruits)
print("Updated List:", capitalized_fruits)