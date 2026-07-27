import numpy as np
import matplotlib.pyplot as plt


def aceleracion(theta):
    return -np.sin(theta)


def rk4_step(theta, omega, dt):
    k1_w = dt * aceleracion(theta)
    k1_t = dt * omega
    k2_w = dt * aceleracion(theta + 0.5 * k1_t)
    k2_t = dt * (omega + 0.5 * k1_w)
    k3_w = dt * aceleracion(theta + 0.5 * k2_t)
    k3_t = dt * (omega + 0.5 * k2_w)
    k4_w = dt * aceleracion(theta + k3_t)
    k4_t = dt * (omega + k3_w)

    omega_new = omega + (k1_w + 2*k2_w + 2*k3_w + k4_w) / 6
    theta_new = theta + (k1_t + 2*k2_t + 2*k3_t + k4_t) / 6
    return theta_new, omega_new


# Configuracion inicial para un angulo > 10 deg
h = 0.01
theta0 = np.radians(60)
omega0 = 0.0

# Deteccion del Periodo Optimo (T_real)
t, th, om = 0.0, theta0, omega0
periodo_real = 0
th, om = rk4_step(th, om, h)
t += h

while t < 20:
    om_prev = om
    th, om = rk4_step(th, om, h)
    t += h
    if om_prev > 0 and om <= 0:  # Pico de amplitud
        periodo_real = t
        break

# Generacion de Secciones de Poincare


def poincare(T_s, muestras=400):
    pth, pom = [], []
    t_c, th_c, om_c = 0.0, theta0, omega0
    for _ in range(muestras):
        t_target = t_c + T_s
        while t_c < t_target:
            dt = min(h, t_target - t_c)
            th_c, om_c = rk4_step(th_c, om_c, dt)
            t_c += dt
        pth.append(th_c)
        pom.append(om_c)
    return pth, pom


pth_lin, pom_lin = poincare(2 * np.pi)
pth_opt, pom_opt = poincare(periodo_real)

# Bosquejo del Espacio de Fases (Trayectoria continua)
traj_th, traj_om = [theta0], [omega0]
th, om = theta0, omega0
for _ in range(int(periodo_real/h) + 1):
    th, om = rk4_step(th, om, h)
    traj_th.append(th)
    traj_om.append(om)

# Visualizacion
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(131)
ax1.plot(traj_th, traj_om, color='gray', alpha=0.5, label='Trayectoria')
ax1.scatter(pth_lin, pom_lin, s=10, color='red', label='Seccion P. (T=2pi)')
ax1.set_title("Deriva de Fase (Regimen No Lineal)")
ax1.legend()
ax1.grid(True)

ax2 = fig.add_subplot(132)
ax2.plot(traj_th, traj_om, color='gray', alpha=0.5)
ax2.scatter(pth_opt, pom_opt, s=40, color='blue',
            edgecolors='black', label='Punto Fijo')
ax2.set_title(f"Periodo Optimo (T = {periodo_real:.3f} s)")
ax2.legend()
ax2.grid(True)

ax3 = fig.add_subplot(133)
# Bosquejo de multiples orbitas para mostrar la topologia
for a in [30, 60, 90, 120]:
    th_b, om_b = np.radians(a), 0.0
    b_th, b_om = [], []
    for _ in range(1000):
        th_b, om_b = rk4_step(th_b, om_b, 0.05)
        b_th.append(th_b)
        b_om.append(om_b)
    ax3.plot(b_th, b_om, label=f'{a} deg')
ax3.set_title("Bosquejo: Espacio de Fases")
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.show()
