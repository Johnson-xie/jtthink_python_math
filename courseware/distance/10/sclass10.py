import  numpy as np
from numpy import dot
from scipy.spatial import distance
A=np.array([100, 140])

B=np.array([60, 120])

C=np.array([70, 130])


print(distance.mahalanobis(A,B,np.linalg.pinv(np.cov(A,B))))



print(distance.mahalanobis(A,C,np.linalg.pinv(np.cov(A,C))))



print(distance.mahalanobis(B,C,np.linalg.pinv(np.cov(B,C))))

delta = A - B

print(np.sqrt(np.dot(np.dot(delta, np.linalg.pinv(np.cov(A, B))), delta)))
