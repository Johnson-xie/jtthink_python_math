import  numpy as np
from scipy.spatial import  distance
v1=np.array([2,4])
v2=np.array([5,2])


print(np.sqrt(np.sum(np.square(v1-v2))))

print(distance.euclidean(v1,v2))