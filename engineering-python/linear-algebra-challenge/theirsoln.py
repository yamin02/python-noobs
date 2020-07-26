#%%
import numpy as np
import matplotlib.pyplot as plt

# setting up the equation
tp = np.array([0.25, 0.5, 0.75, 1])
yp = np.array([3, 2, -3, 0])
A = np.zeros((4, 4))
rhs = np.zeros(4)
for i in range(4):
  A[i] = np.sin(1 * np.pi * tp[i]), np.sin(2 * np.pi * tp[i]), \
      np.sin(3 * np.pi * tp[i]), np.sin(4 * np.pi * tp[i])  # Store one row at a time
  rhs[i] = yp[i]

# Solving the equation
sol = np.linalg.solve(A, rhs)
print('a, b, c, d: ', sol)

# plotting the wave
t = np.linspace(0, 1, 100)
y = sol[0] * np.sin(1 * np.pi * t) + sol[1] * np.sin(2 * np.pi * t) + \
    sol[2] * np.sin(3 * np.pi * t) + sol[3] * np.sin(4 * np.pi * t)
plt.plot(t, y, 'b', label='wave')
plt.xlabel('t')
plt.ylabel('y')

# plotting the initial points
plt.plot(tp, yp, 'ro', label='data')
plt.legend(loc='best');


# %%
