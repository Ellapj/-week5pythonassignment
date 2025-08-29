# Define a base class called Vehicle
class Vehicle:
    def move(self):
        # This is a generic method meant to be overridden
        print("The vehicle is moving.")

# Define a subclass for Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

# Define a subclass for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

# Define a subclass for Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing across the water 🚤")

# Define a subclass for Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling along the path 🚲")

        #example usage.

      # Create a list of different vehicle objects
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Loop through each vehicle and call its move() method
for v in vehicles:
    v.move()