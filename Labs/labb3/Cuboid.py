from Rectangle import Rectangle

class Cuboid(Rectangle):
    
    def __init__(self, x, y, z, width, height, depth):
        super().__init__(x, y, width, height)
        try:
            self.z = float(z)
            self.depth = float(depth)
            self.type = "Cuboid"
        except ValueError:
                return self.error_message()

    def __repr__(self):
        return f"{self.type}: Center position at (x={self.x}, y={self.y}, z={self.z}), width={self.width}, height={self.height}, depth={self.depth}"

    def __eq__(self, other):
        return super().__eq__() and self.depth == other.depth
    
    def volume(self):
        return super().area() * self.depth

    def is_cube(self):
        return self.is_square() and self.depth == self.width
    
    def translate(self, x, y, z):
        super().translate(x, y)
        try:
            self.z += float(z)
        except ValueError:
            return self.error_message()

    def top_right_z(self):
        return super().top_right(), self.z + self.depth / 2
    
    def bot_left_z(self):
        return super().bot_left(), self.z - self.depth / 2
    
    def inside_box_math(self, x, y, z):
        return super().inside_rectangle_math(x,y) and z <= self.top_right_z()[1] and z >= self.bot_left_z()[1]
        
        """
        https://stackoverflow.com/questions/21037241/how-to-determine-a-point-is-inside-or-outside-a-cube
        Hittade denna som supersnyggt visar korrekta sätt att göra detta, inklusive roterade kuboider osv,
        men jag fattar det inte riktigt så kanske skippar just den delen
        """
    