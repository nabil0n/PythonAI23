from Geometry import Geometry
from Rectangle import Rectangle
from Circle import Circle
from Cuboid import Cuboid
from Sphere import Sphere

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from random import choice

COLORS = ["red", "green", "blue", "orange", "purple", "pink", "brown", "black"]

def plot_in_2d(shape):
    
    #plt.figure(0)
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

sph1 = Sphere(0.5, 0.5, 0.5, 0.5)
box1 = Cuboid(0, 0, 0, 2, 5, 3)

# plot_in_2d(r1)
# plot_in_2d(r2)
# plot_in_2d(c1)
# plot_in_2d(c2)

# plt.show()

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


def plot_in_3d(shape, grid_size=5):
    
    if shape.type == "Cuboid":
    # Tror denna grunden för kub (https://www.geeksforgeeks.org/how-to-draw-3d-cube-using-matplotlib-in-python/)
    # Bara att lära sig vad det betyder...
        
        axes = [int(shape.width), int(shape.height), int(shape.depth)]
        data = np.ones(axes, dtype=np.bool_)
        
        alpha = 0.8
        colors = np.empty(axes + [4], dtype=np.float32)
        colors[:] = [1, 0, 0, alpha] # red
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        ax.voxels(data, facecolors=colors)
        
        ax.set_ylim([(shape.y-grid_size), (shape.y+grid_size)])
        ax.set_zlim([(shape.z-grid_size), (shape.z+grid_size)])
        ax.set_xlim([(shape.x-grid_size), (shape.x+grid_size)])
        
        ax.set_zlabel('Z')
        ax.set_xlabel('X')
        ax.set_zlabel('Y')
        
        plt.axis('equal')
    
    elif shape.type == "Sphere":
        
        fig = plt.figure(1)
        ax = fig.add_subplot(111, projection='3d')

        u = np.linspace(0, 2 * np.pi, 10)
        v = np.linspace(0, np.pi, 10)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x+4, y, z+10, linewidth=0.0)
        ax.plot_surface(x+4, y, z, linewidth=0.0)
        
        ax.auto_scale_xyz((0,10), (-5,5), (0,10))


plot_in_3d(box1)
plot_in_3d(sph1)
plt.show()