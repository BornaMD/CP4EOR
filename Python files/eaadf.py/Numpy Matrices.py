import numpy as np

l1 = [1, 2,3,4]
l2 = [1,5,3,6]
l3 = [5,4,6,3]
l4 = [4,5,4,3]


l = np.array([l1,l2,l3,l4])[np.newaxis]
print(l.T)