import numpy as np
import matplotlib.pyplot as plt

# Parámetros
g = 10
v0 = 5
alpha = np.radians(60)

# Ecuación
x = np.linspace(0, 2.3, 500)
y = x * np.tan(alpha) - (g / (2 * v0**2 * np.cos(alpha)**2)) * x**2

# Encontrar el alcance
indice = np.where(y >= 0)[0][-1]
alcance = x[indice]

# Gráfica
plt.plot(x, y)
plt.scatter(alcance, 0)
plt.text(alcance, 0, f'{alcance:.4f}')
plt.grid(True)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Movimiento parabólico - Analítico')

plt.savefig('../images/problem01_1.png', dpi=300, bbox_inches='tight')
plt.show()