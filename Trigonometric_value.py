import math

# Input angle in degrees
angle = float(input("Enter angle in degrees: "))

# Convert degrees to radians
radian = math.radians(angle)

# Calculate sin, cos, and tan
sin_value = math.sin(radian)
cos_value = math.cos(radian)
tan_value = math.tan(radian)

# Display results
print("Sin value:", sin_value)
print("Cos value:", cos_value)
print("Tan value:", tan_value)