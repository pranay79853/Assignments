import random
import string

# Length of the password
length = 12

# Characters to use in the password
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Shuffle the password
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print("Generated Password:", password)