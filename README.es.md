[English](README.md) | Español

# Simulaciones Robóticas

Experimentos de simulación mínima que exploran modelos y algoritmos fundamentales utilizados en sistemas robóticos.

Este repositorio contiene pequeñas simulaciones ejecutables que ilustran cómo los robots móviles se mueven, estiman su estado e interactúan en entornos inciertos. El objetivo es demostrar los **principios básicos de ingeniería que sustentan los algoritmos robóticos** en lugar de desarrollar grandes estructuras de software.

Los experimentos se centran en modelos simplificados comunes en la investigación y la práctica de la ingeniería robótica.

## Contenido

El directorio `simulations/` contiene varios experimentos de robótica mínima:

* `differential_drive_kinematics.py`

Simula el modelo cinemático de un robot de accionamiento diferencial y visualiza la trayectoria resultante.

* `pid_motor_control.py`

Demuestra cómo un controlador PID estabiliza un modelo de motor simple en un sistema de control de lazo cerrado.

* `simple_kalman_localization.py`

Ilustra cómo un filtro de Kalman puede estimar la posición de un robot a partir de mediciones con ruido.

* `occupancy_grid_simulation.py`

Demostración de mapeo probabilístico utilizando una representación simplificada de cuadrícula de ocupación.

## Objetivo

Estos experimentos ilustran conceptos de ingeniería relevantes para:

* Cinemática de robots móviles
* Sistemas de control por retroalimentación
* Estimación probabilística del estado
* Localización de robots
* Representación del entorno

Las simulaciones complementan los repositorios de los **Laboratorios de Robótica y Sistemas**, proporcionando modelos ejecutables que ilustran el comportamiento de los algoritmos robóticos en la práctica.

## Motivación

Los sistemas robóticos operan en entornos dinámicos e inciertos. Los ingenieros deben diseñar algoritmos capaces de estimar estados del sistema, controlar actuadores y construir representaciones internas del mundo.

La simulación es una herramienta esencial para comprender estos algoritmos antes de implementarlos en hardware real. Al experimentar con modelos simplificados, resulta más fácil razonar sobre el comportamiento, la estabilidad y la robustez del sistema.

Este repositorio explora estas ideas mediante experimentos pequeños e interpretables.

## Método

Cada experimento implementa un modelo matemático simplificado, comúnmente utilizado en robótica.

Las simulaciones incluyen:

* Modelos cinemáticos de robots móviles
* Control de lazo cerrado mediante regulación PID
* Estimación probabilística mediante filtrado de Kalman
* Representación del entorno basada en cuadrícula

Las implementaciones son intencionalmente minimalistas y priorizan la claridad sobre la exhaustividad.

El objetivo es exponer la **estructura de los algoritmos robóticos** de una manera que sea fácil de inspeccionar, modificar y experimentar.

## Ejecución de las simulaciones

Clonar el repositorio y ejecutar cualquiera de los scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/robotics-simulations
cd robotics-simulations
python simulations/differential_drive_kinematics.py
```

Algunas simulaciones generan gráficos para visualizar el comportamiento del sistema.

## Ejemplo de salida

![differential drive example](assets/differential-drive-kinematics.png)
![occupancy grid example](assets/occupancy-grid-simulation.png)
![pid motor control example](assets/pid-motor-control.png)
![kalman-localization example](assets/simple-kalman-localization.png)

## Árbol del proyecto

```bash
robotics-simulations
├─ .python-version
├─ README.md
├─ assets
│ ├─ differential-drive-kinematics.png
│ ├─ occupancy-grid-simulation.png
│ ├─ pid-motor-control.png
│ └─ simple-kalman-localization.png
├─ pyproject.toml
├─ src
│ ├─ differential-drive-kinematics.py
│ ├─ occupancy-grid-simulation.py
│ ├─ pid-motor-control.py
│ └─ simple-kalman-localization.py
└─ uv.lock
```

## Requisitos

Los ejemplos usan:

* Python 3.12+
* NumPy
* Matplotlib

## Instalación

Instale las dependencias necesarias:

* using `pip`

```bash
pip install numpy matplotlib
```

* using `uv`

```bash
uv add numpy matplotlib
```

## Referencias

* Thrun, S., Burgard, W. y Fox, D. (2005).
  *Robótica Probabilística.*

* Siegwart, R., Nourbakhsh, I. y Scaramuzza, D. (2011).
  *Introducción a los Robots Móviles Autónomos.*

* Corke, P. (2017).
  *Robótica, Visión y Control.*
