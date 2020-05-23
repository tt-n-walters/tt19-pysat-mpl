import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from ranges import stepped
import math


def y(x):
    return math.sin(x)



figure = plt.figure()
axes = mplot3d.Axes3D(figure)

x_coords = stepped(0, 2 * math.pi, 0.05)
y_coords = [y(x) for x in x_coords]

axes.plot(x_coords, y_coords)

plt.show()

