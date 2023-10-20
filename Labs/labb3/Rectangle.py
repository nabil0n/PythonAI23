from Geometry import Geometry

class Rectangle(Geometry):
    """Rectangle.

    Child instance of Geometry for creation and manipulation of a rectangle.

    Attributes
    ----------
    x, y : float
        Positional coordinates.
    
    width, height : float
        Width and height of our rectangle.
        
    Methods
    ----------
    __eq__ : bool
        Overloads == to instead compare if two heights and widths are the same.
        
    inside_rectangle_math() : bool
        Executes the nessecary math for checking if a point is within the rectangle.
        Is called by parent method: is_inside()
        
    @Properties
    ----------
    get_area : float
        Calculates and returns the area of our rectangle.
    
    get_circumference : float
        Calculates and returns the circumference/perimiter of our rectangel.
        Named circumference for a more general user experience, as sister (Circle)
        has a similar one.
    
    is_square : bool
        Returns whether width is equal to height, and therefore a perfect square.
    
    bot_left, top_right : float
        Returns the (x,y) position for two opposing corners of the rectangle.
        Used by inside_rectangle_math(). See docstring at bottom for remaining two.
    """
    
    def __init__(self, x, y, width, height):
        """Initiializer

        Args:
            x (float): x-coordinate (from parent-class)
            y (float): y-coordinate (from parent-class)
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
            
        Returns:
            str: Name of type of instance ("Rectangle")
            float: x
            float: y
            float: width, and sets it to the negative negative value if negative.
            flaot: height, and sets it to the negative negative value if negative.
            str: Calls the error_message from parent-class if ValueError.
        """
        
        super().__init__(x, y)
        self.type = "Rectangle"
        
        try:
            self.width = float(width) if width > 0 else width*-1
            self.height = float(height) if height > 0 else height*-1
        except ValueError:
            return self.error_message
        
    def __str__(self):
        """String overload

        Returns:
            str: Complete user friendly explaination of created rectangle.
        """
        
        return f"{self.type}: Center position at (x={self.x}, y={self.y}), width={self.width}, height={self.height}"
    
    def __repr__(self):
        """String overload

        Returns:
            str: More dev oriented, cold and short information about the rectangle.
        """
        
        return f"{self.type = }, {self.x = }, {self.y = }, {self.width = }, {self.height = }"

    def __eq__(self, other):
        """Operator overload

        Args:
            other (Rectangle): Any other rectangle within our program.

        Returns:
            bool: True if both rectangles have the same widths and heights.
        """
        
        return True if self.width == other.width and self.height == other.height else False
    
    def inside_rectangle_math(self, x, y):
        """Positional calculator

        Args:
            x (float): x-coordinate
            y (float): y-coordinate

        Returns:
            bool: True if given (x,y) is between the opposite corners of rectangle.
            str: Calls the error_message from parent-class if ValueError.
        """
        
        return x <= self.top_right[0] and self.top_right[1] >= y and x >= self.bot_left[0] and self.bot_left[1] <= y
    
    @property
    def get_area(self):
        """Area calculator

        Returns:
            float: The area of the rectangle.
        """
        
        return self.width * self.height
    
    @property
    def get_circumference(self):
        """Circumference calculator

        Returns:
            float: The circumference of the rectangle.
        """
        
        return self.width * 2 + self.height * 2

    @property
    def is_square(self):
        """Square checker

        Returns:
            bool: True if both sides have equal length.
        """
        
        return True if self.width == self.height else False
    
    @property
    def bot_left(self):
        """Bottom left corner calculator

        Returns:
            tuple: The (x,y) coordinates for the bottom left corner of the rectangle.
        """
        
        return self.x - self.width / 2, self.y - self.height / 2
    
    @property
    def top_right(self):
        """Top right corner calculator

        Returns:
            tuple: The (x,y) coordinates for the top right corner of the rectangle.
        """
        
        return self.x + self.width / 2, self.y + self.height / 2
    
    """
    Not used // The remaining two corner calculations.
    
    def bot_right(self):
        return self.x + self.width / 2, self.y - self.height / 2
    
    def top_left(self):
        return self.x - self.width / 2, self.y + self.height / 2
    """
    