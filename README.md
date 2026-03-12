English | [Español](README.es.md)

# Robotics Simulations

Minimal simulation experiments exploring fundamental models and algorithms used in robotics systems.

This repository contains small executable simulations illustrating how mobile robots move, estimate their state, and interact with uncertain environments. The goal is to demonstrate the **core engineering principles behind robotics algorithms** rather than building large software frameworks.

The experiments focus on simplified models commonly encountered in robotics research and engineering practice.

## Contents

The `simulations/` directory contains several minimal robotics experiments:

* `differential_drive_kinematics.py`

  Simulates the kinematic model of a differential-drive robot and visualizes the resulting trajectory.

* `pid_motor_control.py`

  Demonstrates how a PID controller stabilizes a simple motor model in a closed-loop control system.

* `simple_kalman_localization.py`

  Illustrates how a Kalman filter can estimate the position of a robot from noisy measurements.

* `occupancy_grid_simulation.py`

  Demonstrates probabilistic mapping using a simplified occupancy grid representation.

## Purpose

These experiments illustrate engineering concepts relevant to:

* mobile robot kinematics
* feedback control systems
* probabilistic state estimation
* robot localization
* environment representation

The simulations complement the repositories in the **Robotics & Systems Labs**, providing executable models that illustrate how robotics algorithms behave in practice.

## Motivation

Robotic systems operate in dynamic and uncertain environments. Engineers must design algorithms capable of estimating system states, controlling actuators, and building internal representations of the world.

Simulation is an essential tool for understanding these algorithms before deploying them on real hardware. By experimenting with simplified models, it becomes easier to reason about system behaviour, stability, and robustness.

This repository explores these ideas through small and interpretable experiments.

## Method

Each experiment implements a simplified mathematical model commonly used in robotics.

The simulations include:

* kinematic models of mobile robots
* closed-loop control using PID regulation
* probabilistic estimation using Kalman filtering
* grid-based environment representation

The implementations are intentionally minimal and prioritise clarity over completeness.

The goal is to expose the **structure of robotics algorithms** in a way that is easy to inspect, modify, and experiment with.

## Running the simulations

Clone the repository and run any of the scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/robotics-simulations
cd robotics-simulations
python simulations/differential_drive_kinematics.py
```

Some simulations generate plots to visualize the behaviour of the system.

## Example output

![differential drive example](assets/differential-drive-kinematics.png)
![occupancy grid example](assets/occupancy-grid-simulation.png)
![pid motor control example](assets/pid-motor-control.png)
![kalman-localization example](assets/simple-kalman-localization.png)

## Project tree

```bash
robotics-simulations
├─ .python-version
├─ README.md
├─ assets
│  ├─ differential-drive-kinematics.png
│  ├─ occupancy-grid-simulation.png
│  ├─ pid-motor-control.png
│  └─ simple-kalman-localization.png
├─ pyproject.toml
├─ src
│  ├─ differential-drive-kinematics.py
│  ├─ occupancy-grid-simulation.py
│  ├─ pid-motor-control.py
│  └─ simple-kalman-localization.py
└─ uv.lock
```

## Requirements

The examples use:

* Python 3.12+
* NumPy
* Matplotlib

## Installation

Install the required dependencies:

* using `pip`

```bash
pip install numpy matplotlib
```

* using `uv`

```bash
uv add numpy matplotlib
```

## References

* Thrun, S., Burgard, W., & Fox, D. (2005).
  *Probabilistic Robotics.*

* Siegwart, R., Nourbakhsh, I., & Scaramuzza, D. (2011).
  *Introduction to Autonomous Mobile Robots.*

* Corke, P. (2017).
  *Robotics, Vision and Control.*
