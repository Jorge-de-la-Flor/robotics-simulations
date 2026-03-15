English | [Español](MATHEMATICAL_DERIVATIONS.es.md)

# Mathematical Foundations of Perception and Control

This document provides the formal mathematical derivations for the algorithms implemented in this repository. These derivations bridge the gap between abstract control theory and the discrete-time implementations found in the Python and Rust scripts.

---

## 1. Optimal 1D State Estimation (Kalman Filter)

The implementation in `kalman_filter_localization.py` follows a recursive Bayesian estimation process. We model a system where the state $x$ is subjected to Gaussian noise.

### The System Model

We define the discrete-time evolution of the state $x_k$ and the measurement $z_k$:

1. **Process Model:** $$x_k = x_{k-1} + u_k + w_k, \quad w_k \sim N(0, Q)$$  
   Where $u_k$ is the control input and $w_k$ is the process noise with variance $Q$.

2. **Measurement Model:** $$z_k = x_k + v_k, \quad v_k \sim N(0, R)$$  
   Where $v_k$ is the measurement noise with variance $R$.

### The Recursive Update Logic

The Kalman Filter minimizes the steady-state error covariance $P$. The process is divided into two distinct phases:

**Phase 1: Prediction (A Priori)**
We project the state and uncertainty forward:
$$\hat{x}_{k|k-1} = \hat{x}_{k-1|k-1} + u_k$$
$$P_{k|k-1} = P_{k-1|k-1} + Q$$

**Phase 2: Update (A Posteriori)**
We correct the prediction using the new measurement $z_k$. The optimal Kalman Gain $K$ is derived by minimizing the posterior covariance:
$$K_k = \frac{P_{k|k-1}}{P_{k|k-1} + R}$$

Finally, we update the state estimate and the covariance:
$$\hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k(z_k - \hat{x}_{k|k-1})$$
$$P_{k|k} = (1 - K_k)P_{k|k-1}$$

---

## 2. Differential Drive Kinematics

The simulation in `differential_drive_trajectory.py` models a non-holonomic mobile robot. The relationship between wheel angular velocities and the robot's planar motion is derived as follows.

Given wheel radius $r$ and track width (wheelbase) $b$:

1. **Linear Velocity ($v$):** The average speed of the robot's center.
   $$v = r \frac{\omega_r + \omega_l}{2}$$

2. **Angular Velocity ($\omega$):** The rate of change of the robot's heading.
   $$\omega = r \frac{\omega_r - \omega_l}{b}$$

### State Space Evolution

To find the pose $[x, y, \theta]^T$ at time $t$, we integrate the velocities over a time step $dt$:
$$\dot{x} = v \cos(\theta)$$
$$\dot{y} = v \sin(\theta)$$
$$\dot{\theta} = \omega$$

---

## 3. PID Control Theory

The implementation in `pid_motor_control.py` utilizes a parallel PID structure to minimize the error $e(t) = y_{setpoint} - y(t)$.

The continuous control law is:
$$u(t) = K_p e(t) + K_i \int_{0}^{t} e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

### Discrete-Time Implementation

For digital systems with a sampling time $\Delta t$, the components are approximated as:

- **Proportional:** $K_p e_k$
- **Integral:** $K_i \sum (e_k \Delta t)$ (Accumulated sum)
- **Derivative:** $K_d \frac{e_k - e_{k-1}}{\Delta t}$ (Finite difference)

---

_Note: These derivations serve as the theoretical baseline for the numerical simulations provided in this laboratory._
