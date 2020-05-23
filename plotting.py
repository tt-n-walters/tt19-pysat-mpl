import matplotlib.pyplot as plt
import math

from ranges import stepped


def y(x):
    return math.sin(x)


x_coords = stepped(-10, 10, 0.1)
y_coords = [y(x) for x in x_coords]

y_coords = []
for x in x_coords:
    y_coords.append(y(x))

args = {
    "linestyle": "-.",
    "color": "magenta"
}

plt.plot(x_coords, y_coords, **args)
plt.show()
