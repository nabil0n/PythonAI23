from Circle import Circle
from math import pi

class Sphere(Circle):
    """Sphere.

    Child instance of Circle for creation and manipulation of a sphere.

    Attributes
    ----------
    x, y, z : float
        Positional coordinates.
    
    radius : float
        The spheres radius.
    
    Methods
    ----------
    inside_sphere_math() : float
        Executes the nessecary math for checking if a point is within the sphere.
        Is called by super-parent method: is_inside()
        
    translate(x,y,z) : float(s)
        Allows user to add to x,y,z values to move the shape in its geografical space.
    
    @Properties
    ----------
    get_volume : float
        Calculates and returns the volume of the sphere.
    
    is_unit_sphere : bool
        Returns whether the radius is equal to 1 and if the position (x,y,z) of
        the sphere is at (0,0,0).
    """
    
    def __init__(self, x, y, z, radius):
        """Initiializer

        Args:
            x (float): x-coordinate (from parent-class)
            y (float): y-coordinate (from parent-class)
            z (float): z-coordinate
            radius (float): The radius of the sphere (from parent-class)

        Returns:
            str: Name of type of instance ("Sphere")
            float: x-coordinate
            float: y-coordinate
            float: z-coordinate
            float: radius
            str: Calls the error_message from super-class if ValueError.
        """
        
        super().__init__(x, y, radius)
        self.type = "Sphere"
        
        try:
            self.z = float(z)
        except ValueError:
            return self.error_message
    
    def __str__(self):
        """String overload

        Returns:
            str: Complete user friendly explaination of created sphere.
        """
        
        return super().__str__() + f", z={self.z}"
    
    def __repr__(self):
        """String overload

        Returns:
            str: More dev oriented, cold and short information about the sphere.
        """
        
        return super().__repr__() + f", {self.z = }"
    
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
    
    def inside_sphere_math(self, x, y, z):
        """Positional calculator

        Args:
            x (float): x-coordinate
            y (float): y-coordinate

        Returns:
            float: Returnes the nessecary math to see if (x,y) is inside.
            str: Calls the error_message from parent-class if ValueError.
        """
        try:
            return ((float(x) - self.x)**2) + ((float(y) - self.y)**2) + ((float(z) - self.z)**2) <= self.radius**2
        except ValueError:
            return self.error_message
        
    @property
    def get_volume(self):
        """Volume calculator

        Returns:
            float: The volume of the sphere.
        """
        return (4.0/3.0)*pi*self.radius**3

    @property
    def is_unit_sphere(self):
        """Unit sphere checker

        Returns:
            bool: True if radius = 1 and (x,y,z) = (0,0,0)
        """
        return self.is_unit_circle and self.z == 0
    