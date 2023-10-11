from Geometry import Geometry

class Rectangle(Geometry):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        try:
            self.width = float(width)
            self.height = float(height)
            self.type = "Rectangle"
        except ValueError:
            print("ValueError: Nothing but numbers are accepted as arguments for any value.")
    
    def __repr__(self):
        return f"{self.type}: Center position at (x={self.x}, y={self.y}), width={self.width}, height={self.height}"

    def __eq__(self, other):
        return True if self.width == other.width and self.height == other.height else False
    
    def lower_left(self):
        return self.x - self.width / 2, self.y - self.height / 2
    
    def lower_right(self):
        return self.x + self.width / 2, self.y - self.height / 2
    
    def top_left(self):
        return self.x - self.width / 2, self.y + self.height / 2
    
    def top_right(self):
        return self.x + self.width / 2, self.y + self.height / 2

    def area(self):
        return self.width * self.height
    
    def circumference(self):
        return self.width * 2 + self.height * 2

    def is_square(self):
        return True if self.width == self.height else False
    
    def is_inside(self, x, y):
        return True if x <= self.top_right()[0] and self.top_right()[1] >= y and x >= self.top_left()[0] and self.top_left()[1] >= y and x <= self.lower_right()[0] and self.lower_right()[1] <= y and x >= self.lower_left()[0] and self.lower_left()[1] <= y else False
        