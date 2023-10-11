from Rectangle import Rectangle

class Cuboid(Rectangle):
    
    def __init__(self, x, y, z, width, height, depth):
        super().__init__(x, y, width, height)
        try:
            self.z = float(z)
            self.depth = float(depth)
            self.type = "Cuboid"
        except ValueError:
                    print("ValueError: Nothing but numbers are accepted as arguments for any value.")

    def __repr__(self):
        return f"{self.type}: Center position at (x={self.x}, y={self.y}, z={self.z}), width={self.width}, height={self.height}, depth={self.depth}"

    def __eq__(self, other):
        return super().__eq__() and self.depth == other.depth

    def is_cube(self):
        return self.is_square() and self.depth == self.width
    
    def translate(self, x, y, z):
        super().translate(x, y)
        self.z = z