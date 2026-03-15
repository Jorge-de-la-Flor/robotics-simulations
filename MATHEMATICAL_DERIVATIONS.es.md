[English](MATHEMATICAL_DERIVATIONS.md) | Español

# Fundamentos Matemáticos de la Percepción y el Control

Este documento proporciona las derivaciones matemáticas formales de los algoritmos implementados en este repositorio. Estas derivaciones establecen un puente entre la teoría de control abstracta y las implementaciones en tiempo discreto que se encuentran en los scripts de Python y Rust.

--

## 1. Estimación Óptima de Estado 1D (Filtro de Kalman)

La implementación en `kalman_filter_localization.py` sigue un proceso de estimación bayesiana recursiva. Modelamos un sistema donde el estado $x$ está sujeto a ruido gaussiano.

### Modelo del Sistema

Definimos la evolución en tiempo discreto del estado $x_k$ y la medición $z_k$:

1. **Modelo de Proceso:** $$x_k = x_{k-1} + u_k + w_k, \quad w_k \sim N(0, Q)$$
   Donde $u_k$ es la entrada de control y $w_k$ es el ruido del proceso con varianza $Q$.

2. **Modelo de Medición:** $$z_k = x_k + v_k, \quad v_k \sim N(0, R)$$  
   Donde $v_k$ es el ruido de medición con varianza $R$.

### Lógica de Actualización Recursiva

El Filtro de Kalman minimiza la covarianza del error en estado estacionario $P$. El proceso se divide en dos fases distintas:

**Fase 1: Predicción (A Priori)**
Proyectamos el estado y la incertidumbre:
$$\hat{x}_{k|k-1} = \hat{x}_{k-1|k-1} + u_k$$
$$P_{k|k-1} = P_{k-1|k-1} + Q$$

**Fase 2: Actualización (A Posteriori)**
Corregimos la predicción utilizando la nueva medición $z_k$. La ganancia de Kalman óptima $K$ se obtiene minimizando la covarianza posterior:
$$K_k = \frac{P_{k|k-1}}{P_{k|k-1} + R}$$

Finalmente, actualizamos la estimación del estado y la covarianza:
$$\hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k(z_k - \hat{x}_{k|k-1})$$
$$P_{k|k} = (1 - K_k)P_{k|k-1}$$

---

## 2. Cinemática de accionamiento diferencial

La simulación en `differential_drive_trajectory.py` modela un robot móvil no holonómico. La relación entre las velocidades angulares de las ruedas y el movimiento planar del robot se deriva de la siguiente manera.

Dado el radio de la rueda $r$ y la distancia entre ejes $b$:

1. **Velocidad lineal ($v$):** La velocidad media del centro del robot.
   $$v = r \frac{\omega_r + \omega_l}{2}$$

2. **Velocidad angular ($\omega$):** La tasa de cambio de la dirección del robot.
   $$\omega = r \frac{\omega_r - \omega_l}{b}$$

### Evolución del espacio de estados

Para hallar la pose $[x, y, \theta]^T$ en el instante $t$, integramos las velocidades en un intervalo de tiempo $dt$:
$$\dot{x} = v \cos(\theta)$$
$$\dot{y} = v \sin(\theta)$$
$$\dot{\theta} = \omega$$

---

## 3. Teoría del control PID

La implementación en `pid_motor_control.py` utiliza una estructura PID paralela para minimizar el error $e(t) = y_{setpoint} - y(t)$.

La ley de control continuo es:
$$u(t) = K_p e(t) + K_i \int_{0}^{t} e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

### Implementación en tiempo discreto

Para sistemas digitales con un tiempo de muestreo $\Delta t$, los componentes se aproximan como:

- **Proporcional:** $K_p e_k$
- **Integral:** $K_i \sum (e_k \Delta t)$ (Suma acumulada)
- **Derivativa:** $K_d \frac{e_k - e_{k-1}}{\Delta t}$ (Diferencia finita)

---

_Nota: Estas derivaciones sirven como base teórica para las simulaciones numéricas presentadas en este laboratorio._
