from ProjectPi import PiLeibniz, PiEuler, PiWallis
from math import pi
import matplotlib.pyplot as plt
n = 50
L1, L2, L3, L4 = [], [], [], []
for i in range(n):
    ErrLeibniz = abs(pi-PiLeibniz(i))
    ErrEuler = abs(pi-PiEuler(i))
    ErrWallis = abs(pi-PiWallis(i))
    L1.append(i)
    L2.append(ErrLeibniz)
    L3.append(ErrEuler)
    L4.append(ErrWallis)

plt.plot(L1, L2, "-ro", label = "Erreur Leibniz")
plt.plot(L1, L3, "-bs", label = "Erreur Euler")
plt.plot(L1, L4, "-g^", label = "Erreur Wallis")
plt.legend()
plt.show()
