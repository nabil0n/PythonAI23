from Circle import Circle
from math import pi

class Sphere(Circle):
    
    def __init__(self, x, y, z, radius):
        
        super().__init__(x, y, radius)
        self.type = "Sphere"
        
        try:
            self.z = float(z)
        except ValueError:
            return self.error_message
        

    def __repr__(self):
        return super().__repr__() + f", z={self.z}"
    
    @property
    def get_volume(self):
        return (4.0/3.0)*pi*self.radius**3

    def is_unit_sphere(self):
        return self.is_unit_circle and self.z == 0
    
    def translate(self, x, y, z):
        super().translate(x, y)
        try:
            self.z += float(z)
        except ValueError:
            return self.error_message
    
    def inside_sphere_math(self, x, y, z):
        return super().inside_circle_math(x,y) + ((z - self.z)**2)
        