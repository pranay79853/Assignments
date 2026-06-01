class Dog:
    # Class variable
    animal = "Dog"

    # Constructor with two instance variables
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # Method to display details
    def display(self):
        print("Animal :", Dog.animal)
        print("Breed  :", self.breed)
        print("Name   :", self.name)
        print()


# Creating objects of two different breeds
dog1 = Dog("Labrador", "Buddy")
dog2 = Dog("German Shepherd", "Rocky")

# Displaying details
dog1.display()
dog2.display()