import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = x
xx, yy = np.meshgrid(x, y)
R = np.sqrt(xx**2 + yy**2)
zz = np.sinc(R/np.pi)
fig = plt.figure()
plt.imshow(zz, cmap ="hsv")
plt.colorbar()
plt.tight_layout()
plt.show()
