import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

# [x1, x2], [y1, y2]
fig, ax = plt.subplots()
ax.plot([0, 0], [0, 60.00], color = 'k', linestyle = ':')
ax.plot([8.97, 25.34, 0, 0, -20.01, 8.97], [5.10, 30.25, 56.51, 42.31, 33.20, 5.10],
        color = 'k', linestyle = '-')
ax.plot([0, 8.97], [5.10, 5.10], color = 'k', linestyle = ':')
ax.plot([0, 25.34], [30.25, 30.25], color = 'k', linestyle = ':')
ax.plot([0, -20.01], [33.20, 33.20], color = 'k', linestyle = ':')

# Punkte farbig darstellen
plt.scatter([0, 0], [0, 60.00], color = 'black')
plt.scatter([-20.01, 25.34], [5.10, 56.51], color = 'red')
plt.scatter([0, 0, 0], [5.10, 30.25, 33.20], color = 'green')

# Beschriftung der Achsen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')

plt.show()
