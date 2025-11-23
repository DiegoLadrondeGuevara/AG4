import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # <-- Línea añadida para solucionar el error
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros (Pregunta 3)
L = 0.01
C = 1e-5
R = 0
w0 = 1 / np.sqrt(L * C)

# Función de transferencia G(s) = w0^2 / (s^2 + w0^2)
num = [w0**2]
den = [1, 0, w0**2]
G = signal.TransferFunction(num, den)

# Tiempo
t = np.linspace(0, 0.02, 5000)

# Entradas
u1 = np.ones_like(t)
u2 = np.where(t >= 0.01, 1, 0)
u3 = np.exp(-500 * t) * np.sin(3200 * t)

# Respuestas
t1, y1 = signal.step(G, T=t)
t2, y2, _ = signal.lsim(G, U=u2, T=t)
t3, y3, _ = signal.lsim(G, U=u3, T=t)

# Gráficas
fig, axs = plt.subplots(3, 1, figsize=(7, 9), sharex=True)

axs[0].plot(t1, y1)
axs[0].set_title("Respuesta al escalón unitario u(t)")
axs[0].grid(True)

axs[1].plot(t2, y2)
axs[1].set_title("Respuesta al escalón retrasado u(t - 0.01)")
axs[1].grid(True)

axs[2].plot(t3, y3)
axs[2].set_title("Respuesta a sin(3200 t) e^{-500 t}")
axs[2].set_xlabel("Tiempo (s)")
axs[2].grid(True)

plt.tight_layout()
plt.show()