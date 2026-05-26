# Given dictionary
test_dict = {
    "a": 3,
    "b": 5,
    "c": 3,
    "d": 7,
    "e": 3
}

# Value to check
value = 3

# Find frequency
frequency = list(test_dict.values()).count(value)

# Display result
print("Frequency of", value, "is:", frequency)