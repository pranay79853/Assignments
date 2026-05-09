# ASCII Value Checker

print("=== ASCII Value Checker ===")

# Take input from user
char = input("Enter a character: ")

# Check if user entered exactly one character
if len(char) == 1:
    ascii_value = ord(char) # Convert character to ASCII value
    print(f"The ASCII value of '{char}' is: {ascii_value} ")
else:
    print("Please enter only ONE character.")