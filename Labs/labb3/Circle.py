from math import pi
from Geometry import Geometry

class Circle(Geometry):
    """Circle.

    Child instance of Geometry for creation and manipulation of a circle.

    Attributes
    ----------
    x, y : float
        Positional coordinates.
    
    radius : float
        The circles radius.
    
    Methods
    ----------
    __eq__ : bool
        Overloads == to instead compare if two radiuses are the same.
        
    inside_circle_math() : float
        Executes the nessecary math for checking if a point is within the circle.
        Is called by parent method: is_inside()
        
    @Properties
    ----------
    get_area : float
        Calculates and returns the area of the circle.
    
    get_circumference : float
        Calculates and returns the circumference of the circle.
    
    is_unit_circle : bool
        Returns whether the radius is equal to 1 and if the position (x,y) of
        the circle is at (0,0).
    """
    
    def __init__(self, x, y, radius):
        """Initiializer

        Args:
            x (float): x-coordinate (from parent-class)
            y (float): y-coordinate (from parent-class)
            radius (float): The radius of the circle

        Returns:
            str: Name of type of instance ("Circle")
            str: Calls the error_message from parent-class if ValueError.
        """
        super().__init__(x, y)
        self.type = "Circle"
        
        try:
            self.radius = float(radius)
        except ValueError:
            return self.error_message
    
    def __str__(self):
        """String overload

        Returns:
            str: Complete user friendly explaination of created circle.
        """
        
        return f"{self.type}: Radius={self.radius} with center position at x={self.x}, y={self.y}"
    
    def __repr__(self):
        """String overload

        Returns:
            str: More dev oriented, cold and short information about the circle.
        """
        
        return f"{self.type = }, {self.radius = }, {self.x = }, {self.y = }"
    
    def __eq__(self, other):
        """Operator overload

        Args:
            other (Circle): Any other circle within our program.

        Returns:
            bool: True if both circles have same radius.
        """
        
        return self.radius == other.radius
    
    def inside_circle_math(self, x, y):
        """Positional calculator

        Args:
            x (float): x-coordinate
            y (float): y-coordinate

        Returns:
            float: Returnes the nessecary math to see if (x,y) is inside.
            str: Calls the error_message from parent-class if ValueError.
        """
        
        try:
            return ((float(x) - self.x)**2) + ((float(y) - self.y)**2) <= self.radius**2
        except ValueError:
            return self.error_message

    @property
    def get_area(self):
        """Area calculator

        Returns:
            float: Area of circle.
        """
        
        return pi * self.radius ** 2
    
    @property
    def get_circumference(self):
        """Circumference calculator

        Returns:
            float: Circumference of circle.
        """
        
        return 2 * pi * self.radius

    @property
    def is_unit_circle(self):
        """Unit circle checker

        Returns:
            bool: True if radius = 1 and (x,y) = (0,0)
        """
        
        return True if (self.radius == 1 and self.x == 0 == self.y) else False
