import numpy as np

# Parámetros
g = 10
a = -10
v0 = 5
alpha = np.radians(60)

# Solución analítica
x = np.linspace(0, 2.3, 500)

y = x * np.tan(alpha) - (g / (2 * v0**2 * np.cos(alpha)**2)) * x**2

indice = np.where(y >= 0)[0][-1]
alcance_analitico = x[indice]

# Tamaños de paso
pasos = [0.1, 0.01, 0.001]

for h in pasos:

  # Condiciones iniciales
  vx = v0 * np.cos(alpha)
  vy = v0 * np.sin(alpha)

  x = 0
  y = 0

  px = [x]
  py = [y]

  # Método de Heun
  for t in np.arange(0, 50, h):

    vy_pred = vy + h * a

    y = y + h * (vy + vy_pred) / 2
    x = x + h * vx

    vy = vy_pred

    px.append(x)
    py.append(y)

    if y < 0:
      break

  # Último punto válido
  alcance = px[-2]

  # Error relativo
  error = abs((alcance - alcance_analitico) / alcance_analitico) * 100

  print(f'h = {h}')
  print(f'Alcance numérico = {alcance:.4f} m')
  print(f'Alcance analítico = {alcance_analitico:.4f} m')
  print(f'Error relativo = {error:.4f} %')
  print()