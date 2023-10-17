from Geometry import Geometry

class Rectangle(Geometry):
    
    def __init__(self, x, y, width, height):
        
        super().__init__(x, y)
        self.type = "Rectangle"
        
        try:
            self.width = float(width)
            self.height = float(height)
        except ValueError:
            return self.error_message
        
    
    def __repr__(self):
        return f"{self.type}: Center position at (x={self.x}, y={self.y}), width={self.width}, height={self.height}"

    def __eq__(self, other):
        return True if self.width == other.width and self.height == other.height else False
    
    @property
    def get_area(self):
        return self.width * self.height
    
    @property
    def get_circumference(self):
        return self.width * 2 + self.height * 2

    @property
    def is_square(self):
        return True if self.width == self.height else False
    
    @property
    def bot_left(self):
        return self.x - self.width / 2, self.y - self.height / 2
    
    @property
    def top_right(self):
        return self.x + self.width / 2, self.y + self.height / 2
    
    def inside_rectangle_math(self, x, y):
        return x <= self.top_right[0] and self.top_right[1] >= y and x >= self.bot_left[0] and self.bot_left[1] <= y
    
    """
    Behövs ej
    
    def bot_right(self):
        return self.x + self.width / 2, self.y - self.height / 2
    
    def top_left(self):
        return self.x - self.width / 2, self.y + self.height / 2
    """
    