#%%
#Pie chart
import numpy as np
import matplotlib.pyplot as plt

genre = ['yamin', 'life', 'sohaib', 'hasnu', 'jarjes', 'hasnat']
amount = [100,25,70,75, 20,45]
pieColor=['lightBlue',"springGreen", 'pink']
plt.axis('equal')
# equal to make pi look like circle not an ellipse
plt.pie(amount,labels=genre,autopct='%1.1f%%',colors=pieColor)
#autopct = '%1.1f%%' command shows the percentages to one decimal place
# %%
#Histogram
import numpy as np
import matplotlib.pyplot as plt

n = np.random.randn(10000)
fig, axes = plt.subplots(figsize= (12,8))
plt.hist(n)
axes.set_title("Histogram")
axes.set_xlabel("random values of x")
axes.set_xlim(min(n),max(n))

# %%
#box plot like Candle stick
import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.randint(low=1, high = 100, size= 50)
data2 = np.random.randint(low=1, high= 100 , size= 50)
data = [data1, data2]
fig, axes = plt.subplots(figsize=(12,8))
axes.boxplot(data)
axes.set_title("Box Plot")


# %%
#polar plot
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi , 100)
r = np.sin(50 * theta) * np.cos(50 * theta) 
ax = plt.axes([0.4,0.4,0.8,0.8], polar = True)
# fig = plt.figure()
# ax = fig.add_subplot(111, polar=True) 
ax.plot(theta, r);

#%% 
#fill between two curves
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)
fig, axes = plt.subplots(figsize=(12, 8))
axes.fill_between(x, x**3 , x**2)

# %%
#scatter points
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.random.randint(low=1, high=100, size=100)    # creates a random array of 100 intergers 
axes = plt.axes([1,1,2,2])                                          
# fig, axes = plt.subplots(figsize=(12, 8))
axes.scatter(x, y, marker='.')

# %%
