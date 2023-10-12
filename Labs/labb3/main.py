from Geometry import Geometry
from Rectangle import Rectangle
from Circle import Circle
from Cuboid import Cuboid
from Sphere import Sphere

import matplotlib.pyplot as plt
from random import choice

COLORS = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black"]

fig, ax = plt.subplots()

def rectangle_plotter(x, y, width, height):
    ax.add_patch(plt.Rectangle((x,y), width, height))
    
    plt.show()

def circle_plotter(x,y,r):
    plt.figure(figsize=((r-1),(r+1)))
    ax.add_patch(plt.Circle((x, y), radius = r, color=choice(COLORS)))

    plt.show()

c1 = Circle(0.5, 0.5, 0.2)
c2 = Circle(-0.5, -0.5, 0.2)
r1 = Rectangle(0.5, -0.5, 0.4, 0.5)
r2 = Rectangle(-0.5, 0.5, 0.4, 0.5)


circle_plotter(c1.x, c1.y, c1.radius)
#circle_plotter(c2.x, c2.y, c2.radius)
#rectangle_plotter(r1.x, r1.y, r1.width, r1.height)