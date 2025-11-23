import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy import signal

# parameters
L = 0.01
C = 1e-5
w0 = 1 / np.sqrt(L * C)


def G_from_R(R):
    num = [w0 ** 2]
    den = [1.0, R / L, w0 ** 2]
    return signal.TransferFunction(num, den)


t = np.linspace(0, 0.02, 20001)
u_step = np.ones_like(t)
u_del = np.where(t >= 0.01, 1, 0)
u_trans = np.exp(-500 * t) * np.sin(3200 * t)

Rs = [0, 10, 100]


for R in Rs:
    G = G_from_R(R)
    t1, y1 = signal.step(G, T=t)
    t2, y2, _ = signal.lsim(G, U=u_del, T=t)
    t3, y3, _ = signal.lsim(G, U=u_trans, T=t)

    fig, axs = plt.subplots(3, 1, figsize=(6, 8), sharex=True)
    axs[0].plot(t1, y1)
    axs[0].set_title(f'R={R} Ohm Escalón');
    axs[0].grid()
    axs[1].plot(t2, y2)
    axs[1].set_title('Escalón retrasado');
    axs[1].grid()
    axs[2].plot(t3, y3)
    axs[2].set_title('Señal transitoria');
    axs[2].grid()
    axs[2].set_xlabel('t (s)')

    fig.tight_layout()

plt.show()