import numpy as np
import matplotlib.pyplot as plt
def DiffRect(b, h, D):
    lamda= 630*1.E-9
    k = (2*np.pi)/lamda  # wavelength of light in vaccuum
    a = 30 * 1.E-2  # Side of a square-shaped screen (m)
    # The width of the central maximum along (Ox)
    delta_x = 1.E2 * (2 * lamda * D) / b
    print("Largeur de la tache centrale suivant les x : ", delta_x)
    # The width of the central maximum along (Oy)
    delta_y = 1.E2 * (2 * lamda * D) / h
    print("Largeur de la tache centrale suivant les y : ", delta_y)
    N = 400
    X = np.linspace(-a/2, a/2, N)
    Y = X  # coordinates of screen
    B = (k * b * X) / (2. * D)
    H = (k * h * Y) / (2. * D)  # intermediate variable
    # 2D & 3 D representation
    BB, HH = np.meshgrid(B, H)
    I = ((np.sin(BB) / BB)**2) * ((np.sin(HH) / HH)**2)
    # figure 2D
    plt.imshow(I, cmap='gray', interpolation='bilinear',
                origin='lower', vmin=0, vmax=.005)
    plt.xlabel('$X$', fontsize=12, fontweight='bold')
    plt.ylabel('$Y$', fontsize=12, fontweight='bold')
    plt.title('Diffraction de Fraunhofer par ouverture rectangulaire')