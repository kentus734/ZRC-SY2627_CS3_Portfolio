'''
2. Create the Python code that:

a. Creates three classes: Car, Boat, and Drone with a method move().
    move() in the Car class prints "The car drives on the road."
    move() in the Boat class prints "The boat sails on water."
    move() in the Drone class prints "The drone flies in the sky."

b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the
move() method: vehicle.move().

c. Creates one object of each class.

d. Calls the start_trip() method for each object.
'''

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)
