import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2
'''
fig, ax = plt.subplots()  # Instancia os objetos figura e eixos da classe subplots
ax.plot(x, x**3, 'b--')  # Plota um eixo
ax.plot(x, x**4, 'g--') # Plota um segundo eixo
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Título')
#plt.show()
'''
'''
fig, ax = plt.subplots(nrows=5, ncols=5)  # Gera mais gráficos no mesmo plot
print(type(ax))
# ax[0].plot(x, y, 'b')
# ax[1].plot(x, y**2, 'r')
plt.tight_layout()  # Organiza o layout para que os gráficos não se sobreponham 

'''
# fig = plt.figure(figsize=(8, 4), dpi=100, facecolor='Yellow', edgecolor='Green', frameon=True)
fig, axes = plt.subplots(figsize=(12, 3), facecolor='Blue')
axes.plot(x, y, 'r*-', label='Legenda 1')
axes.plot(x, y**2, 'g--', label='Legenda 2')
axes.set_title('Título', color='red')
fig.savefig('PlotTeste.jpg')
axes.legend(loc=2)  # loc=1 (canto superior direito), 2 - canto superior esquerdo , 3 e 4 inferior esquerdo e direito
plt.show()
