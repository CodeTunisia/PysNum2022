from ProjectPi import PiLeibniz, PiEuler, PiWallis
from math import pi
n = 100
print("i", "ErrLeibniz", "ErrEuler", "ErrWallis", sep = 3*"\t")
for i in range(n):
    ErrLeibniz = abs(pi-PiLeibniz(i))
    ErrEuler = abs(pi-PiEuler(i))
    ErrWallis = abs(pi-PiWallis(i))
    print(i, ErrLeibniz, ErrEuler, ErrWallis, sep =  "\t")