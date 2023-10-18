"""docstring best practices taken from
https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings"""

class Geometry:
    """
    Super-class instance for our geometric shapes program.
    
    This program creates geometric shapes and allow the user to size,
    calculate and translate said shape. It also allows you to check if a given coordinate
    is inside one of the initiated shapes. In addition to this it uses main.py to
    plot the shapes.
    
    Attributes
    ----------
    x and y : float
        the x-coordinate and y-coordinate for the 2D-center of created geometrical shape
        
    error_message : method
        A string to be printed at any Error exception.
    
    Methods
    -----------
    __gt__, __lt__, __ge__, __le__ : bool
        These dunder-methods overloads >, <, >= and <= to instead be used to compare the multidimensional
        size of two given shapes. The == overload exists in class children.
        
    translate(x,y,z) : float(s)
        Allows user to add to x,y,z values to move the shape in its geografical space.
    
    is_inside(x,y,z) : bool
        Allows user to check if given point is inside shape by calling relevant math in children classes.
    
    """
    
    def __init__(self, x, y):
        """Initiializer

        Args:
            x (float): x-coordinate
            y (float): y-coordinate
            
        Returns:
            x (float): x-coordinate
            y (float): y-coordinate
            str: Calls the error_message if ValueError.
        """
        
        try:
            self.x = float(x)
            self.y = float(y)
            
        except ValueError:
            return self.error_message
    
    def __str__(self):
        """String overload

        Returns:
            str: Complete user friendly explaination of created shape.
        """
        
        return f"Unidentified shape: Position at (x={self.x}, y={self.y})"
    
    def __repr__(self):
        """String overload

        Returns:
            str: More dev oriented, cold and short information about the rectangle.
        """
        
        return f"{self.x = }, {self.y = }"
    
    @property
    def error_message(self):
        """Error message printer"""
        
        print("Error: Nothing but numbers are accepted as arguments for any value.")
    
    def __gt__(self, other):
        """Greater than : overload

        Args:
            other (Geometry): Any other shape within our program.

        Returns:
            bool: True if size of self is greater than comparison shape.
        """
        
        if self.type == "Sphere" or self.type == "Cuboid":
            return True if self.get_volume > other.get_volume or self.get_volume > other.get_area else False
        
        return True if self.get_area > other.get_area else False

    def __lt__(self, other):
        """Less than : overload

        Args:
            other (Geometry): Any other shape within our program.

        Returns:
            bool: True if size of self is less than comparison shape.
        """
        
        if self.type == "Sphere" or self.type == "Cuboid":
            return True if self.get_volume < other.get_volume or self.get_volume < other.get_area else False
        
        return True if self.get_area < other.get_area else False
    
    def __ge__(self, other):
        """Greater or equal : overload

        Args:
            other (Geometry): Any other shape within our program.

        Returns:
            bool: True if size of self is greater or equal to comparison shape.
        """
        
        if self.type == "Sphere" or self.type == "Cuboid":
            return True if self.get_volume >= other.get_volume or self.get_volume >= other.get_area else False
        
        return True if self.get_area >= other.get_area else False
    
    def __le__(self, other):
        """Less or equal : overload

        Args:
            other (Geometry): Any other shape within our program.

        Returns:
            bool: True if size of self is less or equal to comparison shape.
        """
        
        if self.type == "Sphere" or self.type == "Cuboid":
            return True if self.get_volume <= other.get_volume or self.get_volume <= other.get_area else False
        
        return True if self.get_area <= other.get_area else False
    
    def translate(self, x, y):
        """Translate position

        Args:
            x (float): value to add to x-position
            y (float): value to add to y-position

        Returns:
            x (float): x-coordinate with added positional value of x
            y (float): y-coordinate with added positional value of y
            str: Calls the error_message if ValueError.
        """
        
        try:
            self.x += float(x)
            self.y += float(y)
        except ValueError:
            return self.error_message
    
    def is_inside(self, x, y, z=None):
        """Check if point is inside

        Args:
            x (float): x-coordinate
            y (float): y-coordinate
            z (float, optional): y-coordinate. Defaults to None.

        Returns:
            bool: True if point indeed is inside shape.
            str: error_message if error
        """
        
        try:
            x = float(x)
            y = float(y)
            z = float(z) if z != None else None
            
            if self.type == "Rectangle":
                return True if self.inside_rectangle_math(x,y) else False
            
            elif self.type == "Circle":
                return True if self.inside_circle_math(x, y) else False
            
            elif self.type == "Cuboid":
                return True if self.inside_box_math(x,y,z) else False
            
            elif self.type == "Sphere":
                return True if self.radius**2 >= self.inside_sphere_math(x,y,z) else False
            
        except:
            return self.error_message
    
    