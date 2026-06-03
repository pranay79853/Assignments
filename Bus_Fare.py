# Parent Class
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


# Child Class
class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        return total_fare + (0.10 * total_fare)  # 10% extra maintenance charge


# Creating Bus object
bus = Bus(50)

print("Bus Capacity:", bus.capacity)
print("Total Bus Fare:", bus.fare())