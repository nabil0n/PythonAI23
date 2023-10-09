from Rectangle import Rectangle
from Circle import Circle
from Cuboid import Cuboid
from Sphere import Sphere

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


fig, ax = plt.subplots()

ax.add_patch(patches.Rectangle(1, 1, 2, 6))

plt.show()