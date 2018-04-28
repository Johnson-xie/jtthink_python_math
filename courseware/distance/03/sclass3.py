import  numpy as np
from  scipy.spatial import distance
p1=np.array([[2,4]])

p2=np.array([[3,3]])


p3=np.array([[5,2]])


print(np.vdot(p1,p2))
print(np.linalg.norm(p1)*np.linalg.norm(p2))

print(np.vdot(p1,p2)/(np.linalg.norm(p1)*np.linalg.norm(p2)))

print(distance.cosine(p1,p2))

print(distance.cdist(p1,p2,metric="cosine"))
print(distance.cdist(p2,p3,metric="cosine"))

prods=np.row_stack((p1,p2,p3))

print(distance.pdist(prods,metric="cosine"))

print(distance.squareform(distance.pdist(prods,metric="cosine")))