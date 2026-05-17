import turtle

# Create turtle object
t = turtle.Turtle()

# Draw square
for i in range(4):
    t.forward(100)   # Move forward by 100 units
    t.right(90)      # Turn right by 90 degrees

# Finish
turtle.done()