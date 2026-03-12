"""
PID motor velocity control simulation.

Simulates a PID controller regulating the velocity of a simple motor
model toward a constant setpoint.
"""

import numpy as np
import matplotlib.pyplot as plt

# PID gains
Kp: float = 2.0
Ki: float = 0.5
Kd: float = 0.1

dt: float = 0.1
steps: int = 200

setpoint: float = 10.0

velocity: float = 0.0
integral: float = 0.0
prev_error: float = 0.0

history: list[float] = []

for _ in range(steps):
    error = setpoint - velocity
    integral += error * dt
    derivative = (error - prev_error) / dt

    control = Kp * error + Ki * integral + Kd * derivative

    # Simple first-order motor model.
    velocity += control * dt

    prev_error = error
    history.append(velocity)

plt.plot(history, label="Velocity")
plt.axhline(setpoint, color="r", linestyle="--", label="Setpoint")
plt.title("PID Motor Control Response")
plt.xlabel("Time step")
plt.ylabel("Velocity")
plt.legend()

# plt.show()  # In WSL we don't have UI
plt.savefig("../assets/pid-motor-control.png")
