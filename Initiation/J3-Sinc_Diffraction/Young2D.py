import matplotlib.pyplot as plt
import numpy as np
def Young2D(a, b, D):
    Lambda = 630e-9 
    L = 30e-2   # Largeur de l'ecran
    x = np.linspace(-L/2, L/2, 200) 
    y = x
    X,Y = np.meshgrid(x,y)  
    # Variables intermidières:
    A = (np.pi*a*1e-3)/(Lambda*D); B = (np.pi*b*1e-3)/(Lambda*D)
    T1 = (np.sin(B*X)/(B*X))**2   # Terme de diffraction
    T2 = 1 + np.cos(2*A*X)        # Terme d'interférence
    I = T1 * T2
    plt.figure(figsize=(5, 5))
    plt.imshow(I, cmap="gray", vmax = 0.3*np.max(I))
    plt.colorbar(shrink = 0.8, aspect = 8)
    
Young2D(0.25, 0.15, 10)