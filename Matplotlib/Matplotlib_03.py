import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 3)
y = x**2

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y,color='Pink', linewidth=10, alpha=0.5, linestyle='--')
ax.plot(x, y**2, 'g*-')

ax.set_xlim([0, 20])  # Ajustar limite de eixo
ax.set_ylim([0, 100])

plt.show()