import os, math
import numpy as np

x=np.ones((3,3))
y=np.ones((3,3))
xi, xj= x.shape
mat=np.zeros((3,3))

for i in range(0,xi):
    for j in range(0,xj):
        mat[i,j]=mat[i,j]+x[i,j]+y[i,j]

print(mat)
