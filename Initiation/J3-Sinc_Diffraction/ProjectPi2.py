from math import sqrt, pi
def PiLeibniz(n):
    s = 0
    for i in range(n+1):
        s += 1/((4*i + 1)*(4*i + 3))
    s = s * 8 
    return s

def PiEuler(n):
    s = 0
    for i in range(1, n+1): 
        s += 1/(i*i)
    s = sqrt(6*s)
    return s
def PiWallis(n):
    p=1
    for i in range(1,n+1):
        p*=(4*i**2)/(4*i**2-1)
    p = 2*p
    return (p)
# écrire un fichier
f1 = open("pi.csv", "w")
f1.write("n; pi Leibniz; pi Euler; pi Wallis \n")
for n in range(1, 301):
    f1.write(str(n) + ";" +str(PiLeibniz(n)) + ";" + str(PiEuler(n)) + ";" + str(PiWallis(n)) + "\n")
f1.close()
# lire le fichier pi.csv
f2 = open("pi.csv", "r")
f2.readline() # lire la ligne courante
N, PiL, PiE, PiW = [], [], [], []
for ligne in f2:
    l = ligne.split(";")
    N.append(int(l[0]))
    PiL.append(float(l[1]))
    PiE.append(float(l[2]))
    PiW.append(float(l[3]))
f2.close()
# traçer les résultats
import matplotlib.pyplot as plt
plt.plot(N, PiL, "-r", label = "Leibniz")
plt.plot(N, PiE, "-b", label = "Euler")
plt.plot(N, PiW, "-g", label = "Wallis")
plt.xlabel("n")
plt.ylabel("Euler(n) ; Leibniz(n) ; Wallis(n)")
plt.legend()
plt.show()
