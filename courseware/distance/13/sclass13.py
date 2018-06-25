import  numpy as np
from scipy.spatial import distance

user1=np.array([1,0,2])
user2=np.array([3,4,1])



common_index=np.intersect1d(np.where(user1!=0),np.where(user2!=0))

mean_user1=user1[np.where(user1!=0)].mean()
mean_user2=user2[np.where(user2!=0)].mean()

s1=np.sum((user1[common_index]-mean_user1)*(user2[common_index] -mean_user2)) #分子部分

s2= np.sqrt(np.sum(np.square(user1[common_index]-mean_user1)) * np.sum(np.square(user2[common_index]-mean_user2)))

print(1-s1/s2)


