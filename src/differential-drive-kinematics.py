"""
Differential drive robot trajectory simulation.

Simulates the 2D pose evolution of a differential drive robot given
constant left and right wheel velocities.
"""

import numpy as np
import matplotlib.pyplot as plt

# Robot parameters
wheel_radius: float = 0.05
wheel_base: float = 0.2

# Wheel angular velocities [rad/s]
v_l: float = 1.0
v_r: float = 1.5

# Simulation time
dt: float = 0.1
steps: int = 100

x, y, theta = 0.0, 0.0, 0.0

trajectory_x: list[float] = []
trajectory_y: list[float] = []

for _ in range(steps):
    # Differential drive kinematics
    v = wheel_radius * (v_r + v_l) / 2.0
    omega = wheel_radius * (v_r - v_l) / wheel_base

    x += v * np.cos(theta) * dt
    y += v * np.sin(theta) * dt
    theta += omega * dt

    trajectory_x.append(x)
    trajectory_y.append(y)

plt.plot(trajectory_x, trajectory_y)
plt.title("Differential Drive Trajectory")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")

# plt.show()  # In WSL we don't have UI
plt.savefig("../assets/differential-drive-kinematics.png")
