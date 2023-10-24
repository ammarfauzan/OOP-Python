class Circle:
    def __init__(self, radius):
        self._radius = radius  # Use a private attribute with an underscore

    # getter method
    @property
    def radius(self):
        return self._radius

    # setter method
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
        
    # calculate the area of the circle
    def area(self):
        return 3.14 * (self.radius ** 2)

# create an instance of the Circle class
circle = Circle(5)

# set the radius of the circle
circle.radius = 20
print(circle.radius) # 

# try to set a negative radius
try:
    circle.radius = -5
except ValueError as ve:
    print(ve) # Radius cannot be negative