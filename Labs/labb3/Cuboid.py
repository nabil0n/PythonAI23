from Rectangle import Rectangle

class Cuboid(Rectangle):
    """Cuboid.

    Child instance of Rectangle for creation and manipulation of a cuboid.

    Attributes
    ----------
    x, y, z : float
        Positional coordinates.
    
    width, height, depth : float
        Width, height and depth.
    
    Methods
    ----------
    __eq__ : bool
        Overloads == to instead compare if two heights, widths and depths are the same.
        
    translate() : float(s)
        Overloads the super-class method with same name, adding a z-value.
        
    inside_box_math() : bool
        Executes the nessecary math for checking if a point is within the cuboid.
        Is called by super-parent method: is_inside()
        
    @Properties
    ----------
    get_volume : float
        Calculates and returns the volume of the cuboid.
    
    is_cube : bool
        Returns whether width is equal to both height and depth, and therefore a perfect cube.
    
    bot_left_close, top_right_far : float
        Returns the (x,y,z) position for two opposing corners of the cuboid.
        Used by inside_box_math().
    """
    
    def __init__(self, x, y, z, width, height, depth):
        """Initiializer

        Args:
            x (float): x-coordinate (from parent-class)
            y (float): y-coordinate (from parent-class)
            z (float): z-coordinate
            width (float): Width (from parent-class).
            height (float): Height (from parent-class).
            depth (float): Depth
            
        Returns:
            str: Name of type of instance ("Cuboid)
            float: x-coordinate
            float: y-coordinate
            float: z-coordinate
            float: width
            float: height
            float: depth
            str: Calls the error_message from parent-class if ValueError.
        """
        
        super().__init__(x, y, width, height)
        self.type = "Cuboid"
        
        try:
            self.z = float(z)
            self.depth = float(depth)
        except ValueError:
                return self.error_message
    
    def __str__(self):
        """String overload

        Returns:
            str: Complete user friendly explaination of created cuboid.
        """
        
        return f"{self.type}: Center position at (x={self.x}, y={self.y}, z={self.z}), width={self.width}, height={self.height}, depth={self.depth}"
    
    def __repr__(self):
        """String overload

        Returns:
            str: More dev oriented, cold and short information about the cuboid.
        """
        
        return super().__repr__() + f", {self.z = }, {self.depth = }"

    def __eq__(self, other):
        """Operator overload

        Args:
            other (Cuboid): Any other cuboid within our program.

        Returns:
            bool: True if both cuboids have the same widths, heights and depths.
        """
        
        return super().__eq__() and self.depth == other.depth
    
    def translate(self, x, y, z):
        """Translate position (overloaded)

        Args:
            x (float): value to add to x-position
            y (float): value to add to y-position
            z (float): value to add to z-position 

        Returns:
            x (float): x-coordinate with added positional value of x
            y (float): y-coordinate with added positional value of y
            z (float): z-coordinate with added positional value of z
            str: Calls the error_message if ValueError.
        """
        
        super().translate(x, y)
        try:
            self.z += float(z)
        except ValueError:
            return self.error_message
    
    def inside_box_math(self, x, y, z):
        """Positional calculator

        Args:
            x (float): x-coordinate
            y (float): y-coordinate
            z (float): z-coordinate

        Returns:
            bool: True if given (x,y,z) is between the opposite corners of the cuboid.
            str: Calls the error_message from parent-class if ValueError.
        """
        try:
            return super().inside_rectangle_math(x,y) and float(z) <= self.top_right_far[1] and float(z) >= self.bot_left_close[1]
        except:
            return self.error_message
        
    @property
    def get_volume(self):
        """Volume calculator

        Returns:
            float: Returns volume of cuboid.
        """
        
        return super().get_area * self.depth

    @property
    def is_cube(self):
        """Cube checker

        Returns:
            bool: True if all sides are the same
        """
        
        return self.is_square and self.depth == self.width
    
    @property
    def bot_left_close(self):
        """Corner calculator

        Returns:
            ((tuple)float): adds z-position to the closer bottom left corner.
        """
        
        return super().bot_left, self.z - self.depth / 2
    
    @property
    def top_right_far(self):
        """Corner calculator

        Returns:
            ((tuple)float): adds z-position to the further away top right corner.
        """
        
        return super().top_right, self.z + self.depth / 2
    