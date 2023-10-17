from Geometry import Geometry
from Rectangle import Rectangle
from Circle import Circle
from Cuboid import Cuboid
from Sphere import Sphere

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
from random import choice

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
r2 = Rectangle(-3, 3, 2, 2)
c1 = Circle(3, -3, 3)
c2 = Circle(-3, -3, 2)

sph1 = Sphere(0.5, 0.5, 0.5, 0.5)
box1 = Cuboid(0.5, 0.5, 0.5, 1, 1, 1)

plot_in_2d(r1)
plot_in_2d(r2)
plot_in_2d(c1)
plot_in_2d(c2)

plt.show()

""" Argument insaxade från Labb_3.pdf

cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
cirkel2 = Circle(x=1,y=1, radius=1)
rektangel = Rectangle(x=0,y=0,side1=1, side2=1)
print(cirkel1==cirkel2) # True
print(cirkel2==rektangel) # False
print(cirkel1.is_inside(0.5, 0.5)) # True
cirkel1.translate(5,5)
print(cirkel1.is_inside(0.5, 0.5)) # False
cirkel1.translate("TRE",5) # ge ValueError med lämplig kommentar

"""


#https://www.tutorialspoint.com/plotting-a-3d-cube-a-sphere-and-a-vector-in-matplotlib

# def plot_in_3d(shape):
    
#     plt.rcParams["figure.figsize"] = [7.00, 3.50]
#     plt.rcParams["figure.autolayout"] = True
#     plt.axis("equal")
#     fig = plt.figure()
#     ax = fig.add_subplot(projection='3d')
    
#     if shape.type == "Sphere":
#         r = shape.radius
#         u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
#         x = shape.x + (np.cos(u) * np.sin(v))
#         y = shape.y + (np.sin(u) * np.sin(v))
#         z = shape.z + (np.cos(v))
#         ax.plot_surface(x, y, z)
        
#     else:
#         r = [-1, 1]
#         for s, e in combinations(np.array(list(product(r, r, r))), 2):
#             if np.sum(np.abs(s-e)) == r[1]-r[0]:
#                 ax.plot3D(*zip(s, e), color="green")
#         ax.set_title("Cube")

# plot_in_3d(sph1)
# plot_in_3d(box1)

# plt.show()