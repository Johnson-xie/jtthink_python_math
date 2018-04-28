import numpy as np
from scipy.spatial import distance

# euclidean 欧氏距离

v1 = np.array([2, 4])
v2 = np.array([5, 2])

# numpy 手动算
print(np.sqrt(np.sum(np.square(v1 - v2))))

# scipy 现成方法
print(distance.euclidean(v1, v2))
