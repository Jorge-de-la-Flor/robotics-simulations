"""
Occupancy grid simulation around a robot.

Simulates random obstacle detections around a robot located at the
center of a 2D grid and accumulates hit counts in each cell.
"""

import numpy as np
import matplotlib.pyplot as plt

size: int = 20
grid = np.zeros((size, size))

robot_x = 10
robot_y = 10

for _ in range(50):
    angle = np.random.uniform(0, 2 * np.pi)
    distance = np.random.randint(1, 6)

    x = int(robot_x + distance * np.cos(angle))
    y = int(robot_y + distance * np.sin(angle))

    if 0 <= x < size and 0 <= y < size:
        grid[x, y] += 1

plt.imshow(grid, cmap="gray", origin="lower")
plt.title("Occupancy Grid Simulation")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label="Hit count")

# plt.show()  # In WSL we don't have UI
plt.savefig("../assets/occupancy-grid-simulation.png")
