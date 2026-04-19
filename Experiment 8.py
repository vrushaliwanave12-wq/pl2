class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

def vehicle_movement(vehicle):
    vehicle.move()

car = Car()
bicycle = Bicycle()

print("Car Movement:")
vehicle_movement(car) 

print("\nBicycle Movement:")
vehicle_movement(bicycle) 