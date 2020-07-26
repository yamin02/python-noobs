#%%
import numpy as np
import matplotlib.pyplot as plt

land_temp = np.array([6, 7, 8, 10, 14, 16, 18, 17, 15, 12, 11, 9])
sea_temp = np.array([4, 5, 10, 11, 12, 16, 19, 18, 14, 10, 8, 5])
month1 = np.linspace(1,12,12)
month = np.array(month1)
monthname = ["Jan","Feb","March","April","May","JUN","July","Aug","Sept","Oct","Nov","dec"]
print(month)
fig, axes = plt.subplots(2,1,figsize=(12,8))
axes[0].plot(month , land_temp , 'r-o',label ="Land Temperature")
axes[0].plot(month , sea_temp , 'g-o',label ="Sea Temperature")
axes[0].set_xticks(month)
axes[0].set_xticklabels(monthname)

axes[1].plot(month , land_temp - sea_temp ,'b-', label = "Difference")
axes[1].set_xticks(month)
axes[1].set_xticklabels(monthname)

axes[0].legend(loc = 2 )
axes[1].legend(loc = 'best')