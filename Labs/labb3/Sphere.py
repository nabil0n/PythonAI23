from Circle import Circle
from math import pi

class Sphere(Circle):
    
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, radius)
        try:
            self.z = float(z)
            self.type = "Sphere"
        except ValueError:
                    print("ValueError: Nothing but numbers are accepted as arguments for any value.")

    def __repr__(self):
        return super().__repr__() + f", z={self.z}"
    
    def volume(self):
        return (4.0/3.0)*pi*self.radius**3

    def is_unit_sphere(self):
        return self.is_unit_circle() and self.z == 0
    
    def translate(self, x, y, z):
        super().translate(x, y)
        self.z += float(z)
    
    def inside_sphere_math(self, x, y, z):
        return super().inside_circle_math(x,y) + ((z - self.z)**2)
        