import numpy as np
import matplotlib.pyplot as plt

# Parámetros
g = 10
v0 = 5
alpha = np.radians(60)

# Valores de x
x = np.linspace(0, 2.3, 500)

# Trayectoria
y = x * np.tan(alpha) - (g / (2 * v0**2 * np.cos(alpha)**2)) * x**2

# Gráfica
plt.plot(x, y)
plt.grid(True)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Movimiento parabólico')

plt.savefig('../images/problem01_1.png', dpi=300, bbox_inches='tight')
plt.show()