from ProjectPi import PiLeibniz, PiEuler, PiWallis
from math import pi
n = 10000
print("i", "ErrLeibniz", "ErrEuler", "ErrWallis", sep = 3*"\t")
for i in range(n):
    ErrLeibniz = abs(pi-PiLeibniz(i))
    if ErrLeibniz <= 0.0001:
        k=i
        break
print(k, "\t", ErrLeibniz)

#    ErrEuler = abs(pi-PiEuler(i))
#    ErrWallis = abs(pi-PiWallis(i))
#    print(i, ErrLeibniz, ErrEuler, ErrWallis, sep =  "\t")
"""
ErrLeibniz = abs(pi-PiLeibniz(n))
ErrEuler = abs(pi-PiEuler(n))
ErrWallis = abs(pi-PiWallis(n))
print(n, ErrLeibniz, ErrEuler, ErrWallis, sep =  "\t")
"""