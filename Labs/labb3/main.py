from Geometry import Geometry
from Rectangle import Rectangle
from Circle import Circle
from Cuboid import Cuboid
from Sphere import Sphere

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from random import choice

"""
# Argument insaxade från Labb_3.pdf

cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
cirkel2 = Circle(x=1,y=1, radius=1)
#rektangel = Rectangle(x=0,y=0,side1=1, side2=1)
print(cirkel1==cirkel2) # True
#print(cirkel2==rektangel) # False
print(cirkel1.is_inside(0.5, 0.5)) # True
cirkel1.translate(5,5)
print(cirkel1.is_inside(0.5, 0.5)) # False
cirkel1.translate("TRE",5) # ge ValueError med lämplig kommentar
"""

# Plotter

COLORS = ["red", "green", "blue", "orange", "purple", "pink", "brown", "black"]

def plot_in_2d(shape):
    
    plt.axis([-10, 10, -10, 10])
    plt.axis("equal")
    
    if shape.type == "Circle":
        x = shape.x
        y = shape.y
        r = shape.radius
        
        plt.gca().add_artist(plt.Circle((x, y), radius = r, color=choice(COLORS)))
    
    else:
        x = shape.x
        y = shape.y
        width = shape.width
        height = shape.height
        
        plt.gca().add_artist(plt.Rectangle((x,y), width, height, color=choice(COLORS)))


r1 = Rectangle(3, 3, 3, 3)
r2 = Rectangle(1, 1, 3, 3)
c1 = Circle(-4, -3, 1)
c2 = Circle(-3, -5, 1.5)

sph1 = Sphere(1, 1, 1, 3)
sph2 = Sphere(-1,-1,-1, 2)
box1 = Cuboid(1, 1, 2, 4.2, 4.2, 4.2)

plot_in_2d(r1)
plot_in_2d(r2)
plot_in_2d(c1)
plot_in_2d(c2)

plt.show()

def plot_in_3d(shape):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    """ Plot Cuboid
    
    https://www.geeksforgeeks.org/how-to-draw-3d-cube-using-matplotlib-in-python/
    
    I can't seem to get it to work with floats, but atleast this way it rounds to closest int. Also no negatives please...
    """
    
    if shape.type == "Cuboid":
        
        axes = [int(shape.width), int(shape.height), int(shape.depth)]
        data = np.ones(axes, dtype=float)

        ax.voxels(data)
        ax.auto_scale_xyz((-8, 8), (-8, 8), (-8, 8))
    
    elif shape.type == "Sphere":
    # https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html

        u = np.linspace(0, 2 * np.pi)
        v = np.linspace(0, np.pi)
        x = shape.radius * np.outer(np.cos(u), np.sin(v)) + shape.x
        y = shape.radius * np.outer(np.sin(u), np.sin(v)) + shape.y
        z = shape.radius * np.outer(np.ones(np.size(u)), np.cos(v)) + shape.z

        ax.plot_surface(x, y, z, linewidth=0.0)
        
    ax.set_zlabel('Z')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    plt.axis('equal')

# plot_in_3d(box1)
# plot_in_3d(sph1)
# plot_in_3d(sph2)
# plt.show()