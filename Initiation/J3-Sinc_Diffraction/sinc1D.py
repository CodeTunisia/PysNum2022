import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sinc(x/np.pi)
plt.plot(x, y,"-b", lw =3)
plt.xlabel("x")
plt.ylabel("sinc(x)")
plt.title("Graphique de la fonction sinc (1D)")
plt.savefig("sinc1D.pdf")
plt.show()
