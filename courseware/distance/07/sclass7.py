import  numpy as np
from scipy.spatial import distance

set1=np.array([
    [1,1,0]
])

set2=np.array([
    [1, 1, 1]
])

print(distance.cdist(set1,set2,"jaccard"))

A= ["zhangsan","lisi"]  # 1,1,0
B= ["zhangsan","lisi","wangwu"] #1,1,1

ints=set(A).intersection(B)
uns=set(A).union(B)
j=len(ints)/len(uns)
print(1-j)