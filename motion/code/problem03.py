import numpy as np
import matplotlib.pyplot as plt

# =========================================================
#  SIMULACIÓN DE 5 CUERPOS GRAVITACIONALES
#  4 masas fijas en vértices del cuadrado de lado a
#  C5: partícula de prueba que orbita bajo su atracción
# =========================================================

# ---------------------------------------------------------
# Parámetros del sistema
# ---------------------------------------------------------
a    = 2       # lado del cuadrado
h    = 0.01    # paso de integración (método de Euler)
tfin = 750     # tiempo final de simulación
x0   = 2       # posición inicial x de C5
y0   = 7       # posición inicial y de C5
vy0  = 0       # velocidad vertical inicial de C5

# ---------------------------------------------------------
# Barrido de velocidades horizontales iniciales de C5
# Se prueban distintos vx0 para encontrar órbitas cerradas
# ---------------------------------------------------------
vx0_list = np.arange(0, 1.4 + 0.02, 0.02)

# ---------------------------------------------------------
# Posiciones fijas de las 4 masas en los vértices
# y radio de colisión para detectar impacto con C5
# ---------------------------------------------------------
vx_vert = np.array([ a/2, -a/2, -a/2,  a/2])
vy_vert = np.array([ a/2,  a/2, -a/2, -a/2])
R_col   = 0.5

# --------------------------------------------------------- 
# Función de aceleración gravitacional sobre C5
# Suma la atracción de las 4 masas fijas en los vértices
# ---------------------------------------------------------
def acel_cuadrado(x, y, a):
    vx = np.array([ a/2, -a/2, -a/2,  a/2])
    vy = np.array([ a/2,  a/2, -a/2, -a/2])
    ax = 0.0
    ay = 0.0
    for k in range(4):
        dx = x - vx[k]
        dy = y - vy[k]
        r3 = (dx**2 + dy**2)**1.5
        ax = ax - dx / r3
        ay = ay - dy / r3
    return ax, ay

# ---------------------------------------------------------
# Simulación con método de Euler para cada vx0
# Se integra la trayectoria de C5 y se descarta si impacta
# ---------------------------------------------------------
trayectorias = []

for vx0 in vx0_list:
    x  = x0
    y  = y0
    vx = vx0
    vy = vy0
    px = [x]
    py = [y]
    impacto = False

    for t in np.arange(0, tfin, h):
        ax, ay = acel_cuadrado(x, y, a)

        vx = vx + ax * h
        x  = x  + vx * h
        vy = vy + ay * h
        y  = y  + vy * h

        for i in range(4):
            if np.sqrt((x - vx_vert[i])**2 + (y - vy_vert[i])**2) <= R_col:
                impacto = True
                break
        if impacto:
            break

        px.append(x)
        py.append(y)

    if not impacto and len(px) > 1:
        px = np.array(px)
        py = np.array(py)
        dist     = np.sqrt((px[1:] - x0)**2 + (py[1:] - y0)**2)
        min_dist = np.min(dist)
        trayectorias.append({
            'vx0':      vx0,
            'px':       px,
            'py':       py,
            'dist_min': min_dist
        })

# ---------------------------------------------------------
# Seleccionar las 5 trayectorias más cerradas
# ---------------------------------------------------------
trayectorias.sort(key=lambda t: t['dist_min'])
N_cerradas = min(5, len(trayectorias))
candidatas = trayectorias[:N_cerradas]

# ---------------------------------------------------------
# Figura — trayectorias de C5 + masas fijas
# ---------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(10, 8))
fig.patch.set_facecolor('k')
ax1.set_facecolor('k')
ax1.tick_params(colors='w')
ax1.xaxis.label.set_color('w')
ax1.yaxis.label.set_color('w')
ax1.title.set_color('w')
for spine in ax1.spines.values():
    spine.set_edgecolor([0.3, 0.3, 0.3])
ax1.grid(True, color=[0.3, 0.3, 0.3])
ax1.set_aspect('equal')

colores = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.5, 1.0],
    [1.0, 0.0, 1.0],
    [1.0, 1.0, 0.0]
]
for i, tray in enumerate(candidatas):
    ax1.plot(tray['px'], tray['py'],
             color=colores[i], linewidth=1.5,
             label=f"$v_{{x0}}$ = {tray['vx0']:.2f}")

# Cuadrado punteado que une los 4 vértices
vx_cierre = np.append(vx_vert, vx_vert[0])
vy_cierre = np.append(vy_vert, vy_vert[0])
ax1.plot(vx_cierre, vy_cierre, 'w--', linewidth=1.2)

# 4 masas fijas: círculo relleno
theta = np.linspace(0, 2 * np.pi, 200)
colores_masas = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.5, 1.0],
    [1.0, 0.0, 1.0]
]
for i in range(4):
    cx = vx_vert[i] + R_col * np.cos(theta)
    cy = vy_vert[i] + R_col * np.sin(theta)
    ax1.fill(cx, cy, color=colores_masas[i], edgecolor='w', linewidth=1.0)

# C5: partícula de prueba en el centro (blanco)
ax1.fill(R_col * np.cos(theta), R_col * np.sin(theta),
         color='w', edgecolor=[0.7, 0.7, 0.7], linewidth=1.0)

ax1.set_xlim(-12, 12)
ax1.set_ylim(-10, 10)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Trayectorias cerradas alrededor de cuatro masas')
ax1.legend(facecolor='k', labelcolor='w', edgecolor=[0.3, 0.3, 0.3],
           loc='best')

plt.tight_layout()
plt.savefig('images/problem03.png', dpi=150,
            facecolor=fig.get_facecolor(), bbox_inches='tight')
plt.show()