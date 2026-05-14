num = input("Enter a number: ")

# Remove negative sign if present
if num[0] == '-':
    num = num[1:]

print("Total digits are:", len(num))