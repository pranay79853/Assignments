# Function to calculate circumference of a circle
def circumference(radius):
    return 2 * 3.14 * radius

# Taking input from user
r = float(input("Enter the radius of the circle: "))

# Calling the function
result = circumference(r)

# Displaying the result
print("Circumference of the circle is:", result)