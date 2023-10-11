from math import pi
from Geometry import Geometry

class Circle(Geometry):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        try:
            self.radius = float(radius)
            self.type = "Circle"
        except ValueError:
            print("ValueError: Nothing but numbers are accepted as arguments for any value.")
            
    def __repr__(self):
        return f"{self.type}: Radius={self.radius} with center position at x={self.x}, y={self.y}"
    
    def __eq__(self, other):
        return self.radius == other.radius

    def area(self):
        return pi * self.radius ** 2
    
    def circumference(self):
        return 2 * pi * self.radius

    def is_unit_circle(self):
        return True if (self.radius == 1 and self.x == 0 == self.y) else False
    
    def is_inside(self, x, y):
        return True if ((x - self.x)**2) + ((y - self.y)**2) <= self.radius**2 else False #https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
    