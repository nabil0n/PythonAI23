from Circle import Circle

class Sphere(Circle):
    
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, radius)
        self.z = float(z)
        self.type = "Sphere"
    
    def __repr__(self):
        return super().__repr__() + f", z={self.z}"

    def is_unit_sphere(self):
        return self.is_unit_circle() and self.z == 0
    
    def translate(self, x, y, z):
        super().translate(x, y)
        self.z = float(z)