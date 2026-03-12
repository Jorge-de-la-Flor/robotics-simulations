"""
1D Kalman filter localization example.

Simulates a simple constant-velocity motion model and estimates the
true position from noisy measurements using a 1D Kalman filter.
"""

import numpy as np
import matplotlib.pyplot as plt

# True position
x: float = 0.0

# Estimate
x_est: float = 0.0
P: float = 1.0

Q: float = 0.01  # Process noise variance
R: float = 0.5   # Measurement noise variance

true_positions: list[float] = []
estimates: list[float] = []
measurements: list[float] = []

for _ in range(100):
    # True motion: constant increment of 1 per step.
    x += 1.0

    # Noisy measurement
    z = x + np.random.normal(0, R)

    # Prediction
    x_pred = x_est + 1.0
    P_pred = P + Q

    # Update
    K = P_pred / (P_pred + R)
    x_est = x_pred + K * (z - x_pred)
    P = (1 - K) * P_pred

    true_positions.append(x)
    estimates.append(x_est)
    measurements.append(z)

plt.plot(true_positions, label="True")
plt.plot(measurements, ".", label="Measurement")
plt.plot(estimates, label="Estimate")
plt.legend()
plt.title("Kalman Filter Localization")
plt.xlabel("Time step")
plt.ylabel("Position")

# plt.show()  # In WSL we don't have UI
plt.savefig("../assets/simple-kalman-localization.png")
