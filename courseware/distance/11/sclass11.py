import  numpy as np
from numpy import dot
from scipy.spatial import distance


A=np.array([200,10000,20])
B=np.array([150,20000,40])

x=np.vstack([A,B])
#
# print(x.T.mean(axis=1))

s=np.std(x.T,axis=1,ddof=1) ##标准差

print(np.sqrt(np.sum(np.square((A-B)/s))))

print(distance.pdist(x,metric="seuclidean"))

print(distance.cdist(np.array([A]),np.array([B]),metric="seuclidean"))

print(distance.seuclidean(A,B,s**2))
