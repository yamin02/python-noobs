import numpy.random as rnd
import numpy as np

# same seed produce same random no
# np.seed(14324)
# arr = np.arange(1,5)
arr= ['yamin', 'faraj','benzo','gundo']
pick = rnd.choice(arr, 3 , replace= False)
print(rnd.randint(0, 2, 10))
print(pick)