import numpy as np

a = np.array([[1, 2, 3, 4],
              [6, 7, 8, 9]])
print(a.shape)
print(a.reshape(1, -1))
print(a.reshape(-1,1))
print(a.reshape(-1,2))
print(a.reshape(-1,4))
print(a.reshape(2,-1))
print(a.reshape(4,-1))