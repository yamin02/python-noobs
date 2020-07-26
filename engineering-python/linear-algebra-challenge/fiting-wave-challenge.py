#%%
import numpy as np 
import matplotlib.pyplot as plt


t = np.array([0.25 , 0.5, 0.75 , 1])
acoff = np.sin(1* np.pi* t)
bcoff = np.sin(2* np.pi* t)
ccoff = np.sin(3* np.pi* t)
dcoff = np.sin(4* np.pi* t)
allcoff =np.array([acoff , bcoff, ccoff , dcoff])
y = np.array([3,2,-3,0])

soln = np.linalg.solve(allcoff,y)
print(soln) 

time = np.linspace(-2,2,100)
func = soln[0]*np.sin(1*np.pi *time) + soln[1]*np.sin(2*np.pi *time)+ \
    soln[2]*np.sin(3*np.pi *time)+soln[3]*np.sin(4*np.pi *time)

axis = plt.axes([1,1,2,2])
axis.plot(time,func,color='green',marker = "+",label = 'ki sundor moja')
axis.legend(loc = 'best')
axis.set_xlabel('Time')
axis.set_ylabel('The Function')
axis.set_title("The Fitting Wave")



# %%
