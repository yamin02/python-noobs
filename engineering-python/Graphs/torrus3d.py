#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

def torrus(r, R, theta , phi):
    x = (R + r* np.cos(theta))* np.cos(phi)
    y = (R + r* np.cos(theta)) * np.sin(phi)
    z = (r * np.sin(theta))
    return x, y, z

angle = np.linspace(0, 2 * np.pi , 100)
theta, phi = np.meshgrid(angle,angle)
x1,y1,z1 = torrus(1,2, theta, phi)
fig= plt.figure(figsize = (12,8))
ax = fig.add_subplot(211, projection = '3d')
ax.plot_surface(x1,y1,z1 , cmap = cm.cool)
ax.view_init(35,35)
ax.set_xlim(-3,3)
ax.set_zlim(-3,3)
ax.set_ylim(-3,3)

x2,y2,z2 = torrus(1,3, theta, phi)
ax2 = fig.add_subplot(212, projection = '3d')
ax2.plot_surface(x2,y2,z2 , cmap = cm.rainbow)
ax2.set_xlim(-3,3)
ax2.set_zlim(-3,3)
ax2.set_ylim(-3,3)
ax2.view_init(35,35)
fig.tight_layout()
# %%
