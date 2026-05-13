import numpy as np
import matplotlib.pyplot as plt

# Parámetros
a = -10
v0 = 5
alpha = np.radians(60)

vx = v0 * np.cos(alpha)
vy = v0 * np.sin(alpha)

x = 0
y = 0

h = 0.01
tfin = 50

px = [x]
py = [y]

for t in np.arange(0, tfin, h):

  vy_pred = vy + h * a

  y = y + h * (vy + vy_pred) / 2
  x = x + h * vx

  vy = vy_pred

  px.append(x)
  py.append(y)

  if y < 0:
    break

# Último punto físico válido
alcance = px[-2]

# Gráfica
plt.plot(px, py)
plt.scatter(alcance, 0)
plt.text(alcance, 0, f'{alcance:.4f}')
plt.grid(True)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Movimiento parabólico - Método de Heun')

plt.savefig('../images/problem01_2.png', dpi=300, bbox_inches='tight')
plt.show()