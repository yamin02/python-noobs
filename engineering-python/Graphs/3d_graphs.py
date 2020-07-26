#%%
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# a,b, and c are constants
def spiral(a, b, t):
    x = a * np.cos(t)
    y = a * np.sin(t)
    z = b * t
    return x, y, z

t = np.linspace(0, 20, 100)
x1, y1, z1 = spiral(4, 1, t)
x2, y2, z2 = spiral(2, 2, t)

#fig = plt.figure()
#fig, ax = plt.subplots(figsize=(12,8), projection='3d')
ax = plt.axes([1,1,2,2] , projection = '3d')
ax.plot(x1, y1, z1)
ax.plot(x2, y2, z2)


# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
def func(x,y):
    z = np.sin(np.sqrt(x ** 2 + y ** 2))
    return z
x = np.linspace(0,3,10)
y = np.linspace(5,4 ,3)
X,Y = np.meshgrid(x,y)
Z = func(X,Y)
axis = plt.axes([1,1,2,2], projection="3d" )
axis.plot_surface(X,Y,Z, cmap= cm.cool)  #collor map is cool from cm(color map)
axis.view_init(30,90)
print(Y)
