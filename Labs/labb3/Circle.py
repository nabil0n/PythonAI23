from math import pi
from Geometry import Geometry

class Circle(Geometry):
    
    def __init__(self, x, y, radius):
        
        super().__init__(x, y)
        self.type = "Circle"
        
        try:
            self.radius = float(radius)
        except ValueError:
            return self.error_message
        
            
    def __repr__(self):
        return f"{self.type}: Radius={self.radius} with center position at x={self.x}, y={self.y}"
    
    def __eq__(self, other):
        return self.radius == other.radius

    @property
    def get_area(self):
        return pi * self.radius ** 2
    
    @property
    def get_circumference(self):
        return 2 * pi * self.radius

    @property
    def is_unit_circle(self):
        return True if (self.radius == 1 and self.x == 0 == self.y) else False
    
    def inside_circle_math(self, x, y):
        return ((x - self.x)**2) + ((y - self.y)**2) # (Uppdelad för att funka med sphere)
