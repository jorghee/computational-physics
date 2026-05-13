import numpy as np
import matplotlib.pyplot as plt
# Parámetros del sistema  
G    = 1.0
m    = 1.0
m5   = 5.0
a    = 2.0
eps  = 0.15
h    = 0.002
tfin = 15

# Función de aceleraciones
def aceleraciones(rx, ry, masas, G, eps):
    N  = len(masas)
    ax = np.zeros(N)
    ay = np.zeros(N)
    for i in range(N):
        for j in range(N):
            if i != j:
                dx    = rx[j] - rx[i]
                dy    = ry[j] - ry[i]
                r3    = (dx**2 + dy**2 + eps**2)**1.5
                ax[i] = ax[i] + G * masas[j] * dx / r3
                ay[i] = ay[i] + G * masas[j] * dy / r3
    return ax, ay

# Condiciones iniciales
#   C1:(+a/2,+a/2)  C2:(-a/2,+a/2)
#   C3:(-a/2,-a/2)  C4:(+a/2,-a/2)  C5:(0,0)
masas = np.array([m, m, m, m, m5])
N     = 5

rx = np.array([ a/2, -a/2, -a/2,  a/2,  0.0])
ry = np.array([ a/2,  a/2, -a/2, -a/2,  0.0])

R     = a / np.sqrt(2)
v_orb = 0.80 * np.sqrt(G * np.sum(masas) / R)

vx = np.array([-v_orb,  v_orb,  v_orb, -v_orb,  0.0])
vy = np.array([ v_orb,  v_orb, -v_orb, -v_orb,  0.0])

# Inicializar arreglos
nmax = int(round(tfin / h)) + 2
prx  = np.zeros((N, nmax))
pry  = np.zeros((N, nmax))

n = 0
prx[:, 0] = rx
pry[:, 0] = ry

# Método de Euler
for t in np.arange(0, tfin - h, h):
    n += 1
    ax, ay = aceleraciones(rx, ry, masas, G, eps)
    vx = vx + ax * h
    vy = vy + ay * h
    rx = rx + vx * h
    ry = ry + vy * h
    prx[:, n] = rx
    pry[:, n] = ry

prx = prx[:, :n+1]
pry = pry[:, :n+1]

# FIGURA 
colores = [
    [0.2, 0.5, 1.0],
    [1.0, 0.3, 0.3],
    [0.2, 0.9, 0.4],
    [1.0, 0.7, 0.1],
    [0.8, 0.3, 1.0]
]
nombres = ['C1 (+,+)', 'C2 (-,+)', 'C3 (-,-)', 'C4 (+,-)', 'C5 centro']

fig, ax1 = plt.subplots(figsize=(12, 10))
fig.patch.set_facecolor([0.05, 0.05, 0.08])
ax1.set_facecolor([0.05, 0.05, 0.08])
ax1.tick_params(colors=[0.5, 0.5, 0.5])
ax1.xaxis.label.set_color([0.75, 0.75, 0.75])
ax1.yaxis.label.set_color([0.75, 0.75, 0.75])
for spine in ax1.spines.values():
    spine.set_edgecolor([0.25, 0.25, 0.25])
ax1.grid(True, color=[0.25, 0.25, 0.25], alpha=0.5)
ax1.set_aspect('equal')

for i in range(N):
    c = colores[i]
    # Estela tenue
    ax1.plot(prx[i, :], pry[i, :], '-',
             color=c + [0.4], linewidth=1.0)
    # Cola brillante: último 25%
    k0 = int(round(0.75 * n))
    ax1.plot(prx[i, k0:], pry[i, k0:], '-',
             color=c + [1.0], linewidth=2.0, label=nombres[i])

for i in range(N):
    ax1.plot(prx[i, 0], pry[i, 0], 'o',
             markersize=9, markerfacecolor=colores[i],
             markeredgecolor='k', markeredgewidth=1.2)

for i in range(N):
    ax1.plot(prx[i, -1], pry[i, -1], 'p',
             markersize=12, markerfacecolor=colores[i],
             markeredgecolor='k', markeredgewidth=1.0)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Trayectorias — 5 Cuerpos Gravitacionales',
              color='w', fontsize=14)
ax1.legend(loc='upper right')

plt.tight_layout()
plt.savefig('images/problem03.png', dpi=150,
            facecolor=fig.get_facecolor(), bbox_inches='tight')
plt.show()