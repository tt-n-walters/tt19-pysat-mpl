import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from ranges import stepped
import math

x_coords = stepped(0, 2 * math.pi, 0.05)

def y(x):
    return math.sin(x)



