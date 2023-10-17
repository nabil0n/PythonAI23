class Geometry:
    
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
            
        except ValueError:
            return self.error_message
            
    # def __str__(self):
    #     return f"{self.x}, {self.y}"
    
    def __repr__(self):
        return f"Shape: Position at (x={self.x}, y={self.y})"
    
    def __gt__(self, other):
        if self.type == "Sphere" or self.type == "Cuboid":
            return True if self.get_volume > other.get_volume or self.get_volume > other.get_area else False
        
        return True if self.get_area > other.get_area else False
    
    def __ge__(self, other):
        if self.type == "Sphere" or self.type == "Cuboid":
            return True if self.get_volume >= other.get_volume or self.get_volume >= other.get_area else False
        
        return True if self.get_area >= other.get_area else False
    
    """
        Python själv räknar ut att om > overload redan fanns overloadas < automatiskt.
    """
    
    @property
    def error_message(self):
        print("ValueError: Nothing but numbers are accepted as arguments for any value.")

    def translate(self, x, y):
        try:
            self.x += float(x)
            self.y += float(y)
        except ValueError:
            return self.error_message
    
    def is_inside(self, x, y, z=None):
        
        if self.type == "Rectangle":
            return True if self.inside_rectangle_math(x,y) else False
        
        elif self.type == "Circle":
            return True if self.radius**2 >= self.inside_circle_math(x, y) else False
        
        elif self.type == "Cuboid":
            return True if self.inside_box_math(x,y,z) else False
        
        elif self.type == "Sphere":
            return True if self.radius**2 >= self.inside_sphere_math(x,y,z) else False
    
    