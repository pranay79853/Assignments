class BMW:
    def fuel_type(self):
        print("BMW uses Petrol/Diesel.")

    def max_speed(self):
        print("BMW maximum speed is 250 km/h.")


class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Premium Petrol.")

    def max_speed(self):
        print("Ferrari maximum speed is 340 km/h.")


# Polymorphism
for car in (BMW(), Ferrari()):
    car.fuel_type()
    car.max_speed()
    print()