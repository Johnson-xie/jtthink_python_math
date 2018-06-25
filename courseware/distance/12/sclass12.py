import  numpy as np


from  scipy.spatial import distance
user1=np.array([2,1,2])
user2=np.array([5,4,4])


# print(distance.pdist(np.vstack([user1,user2]),metric="cosine")) #距离  =1-cosine 0.02

user1=user1-user1.mean()
user2=user2-user2.mean()
print(distance.pdist(np.vstack([user1,user2]),metric="cosine")) #距离  =1-cosine  0.5


