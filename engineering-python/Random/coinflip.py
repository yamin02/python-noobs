#%%
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as  plt

#outcome : 2 or if more use for loop in len(flips[flips==i)
flips= rnd.randint(0,3,100)
head=0
tail=0
#print('Head: ' + str(len(flips[flips==0])))
#print("tail: " + str(len(flips[flips == 2])))

rnd.seed(55)

#flip coins multiple(n) times 
n_times = 2
flips1 = rnd.randint(0,2,size=(n_times,100))
tails = np.sum(flips1 , axis=0)  #add the rows 
pos_combinations = 3 # O tails , 2 tails , 1 tails
number_of_tails = np.zeros(pos_combinations, dtype='int')
#print(tails)

for i in range(3):
	number_of_tails[i] = np.count_nonzero(tails ==i)

print('number of 0 tails:', number_of_tails[0])
print('number of 1 tail:', number_of_tails[1])
print('number of 2 tails:', number_of_tails[2])


probality = number_of_tails /100
# So cumulative_prob[0] = prob[0], cum_prob[1] = prob[0] + prob[1], etc.
cumulative_prob = np.cumsum(probality)
print(cumulative_prob)