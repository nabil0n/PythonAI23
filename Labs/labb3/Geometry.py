class Geometry:
    
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
            
        except ValueError:
            print("ValueError: Nothing but numbers are accepted as arguments for any value.")
            
    # def __str__(self):
    #     return f"{self.x}, {self.y}"
    
    def __repr__(self):
        return f"Shape: Position at (x={self.x}, y={self.y})"
    
    def __gt__(self, other):
        if self.type == "Sphere" or self.type == "Cuboid":
            return True if self.volume() > other.volume() or self.volume() > other.area() else False
        
        return True if self.area() > other.area() else False
    
    def __ge__(self, other):
        if self.type == "Sphere" or self.type == "Cuboid":
            return True if self.volume() >= other.volume() or self.volume() >= other.area() else False
        
        return True if self.area() >= other.area() else False

    def translate(self, x, y):
        self.x += float(x)
        self.y += float(y)
    
    def is_inside(self, x, y, z=None):
        
        if self.type == "Rectangle":
            return True if self.inside_rectangle_math(x,y) else False
        
        elif self.type == "Circle":
            return True if self.radius**2 >= self.inside_circle_math(x, y) else False
        
        elif self.type == "Cuboid":
            return True if self.inside_box_math(x,y,z) else False
        
        elif self.type == "Sphere":
            return True if self.radius**2 >= self.inside_sphere_math(x,y,z) else False
    
    
        """
        Haha, hade vart kul om det nedanför funkade. Hittade en annan lösning, men också sen att Python själv
        räknade ut att om > overload redan fanns overloads < automatiskt.
        
    def __lt__(self, other):
        return False if self.__gt__() else True
        
        """