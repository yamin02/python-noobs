import numpy as np

A = np.array([[1,4,5] , 
              [1,2,3] , 
              [5,8,1]])
eigenvalue, eigenvector = np.linalg.eig(A)

B = np.array([[1+3j, 4+3j,3],[5.76+3j, 4+3j,5.76],[1+3j, 5.76+3j,3]])
ehval , ehvec = np.linalg.eigh(B)

ainv = np.linalg.inv(A)
p =np.dot(ainv,A)

determinant = np.linalg.det(p)