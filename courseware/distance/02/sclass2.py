import  numpy as np
from scipy.spatial import distance,distance_matrix
prods=np.array([
        [100,300,10,20],
        [120,500,30,30],
        [80,400,15,50],
        [150,250,8,10],
        [90,380,15,40],
])

bestProds=np.max(prods.T,axis=1)  #最牛逼商品

for index,arr in enumerate(prods.tolist()):
        print("序号:"+str(index)+"距离="+str(distance.euclidean(arr,bestProds)))

print(distance_matrix(prods,np.array([bestProds])))