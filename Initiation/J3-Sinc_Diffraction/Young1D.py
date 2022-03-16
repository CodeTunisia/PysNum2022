import numpy as np
import matplotlib.pyplot as plt
def Young(a, b, D):
    Lambda = 632e-9
    L = 30e-2   # Largeur de l'ecran (m)
    x = np.linspace(-L/2, L/2, 200)   
    # Variables intermidières:
    A = (np.pi*a*1e-3)/(Lambda*D); B = (np.pi*b*1e-3)/(Lambda*D)
    T1 = (np.sin(B*x)/(B*x))**2   # Terme de diffraction
    T2 = 1 + np.cos(2*A*x)        # Terme d'interférence
    I = T1 * T2
    plt.figure(figsize = (7, 4))
    plt.plot(x*1e2, I/max(I), '-r',lw =2, label = "Interférence")
    plt.plot(x*1e2, T1, '--k',lw =2, label = "Diffraction")
    plt.xlabel("x [cm]")
    plt.ylabel("I/I0")
    plt.legend()
    # Tache centrale
    DS = (2*Lambda*D)/(b*1e-3); Ds = (Lambda*D)/(a*1e-3)
    print(" Largeur de la tache centrale = {:.2f} cm".format(DS*1e2))
    print(" Largeur  de l'interfrange = {:.2f} cm".format(Ds*1e2))
Young(0.5, 0.15, 10)    