import  numpy as np
import pandas as pd
from scipy.spatial import distance,distance_matrix

prods=np.array([
        [100,300,10,20],
        [120,500,30,30],
        [80,400,15,50],
        [150,250,8,10],
        [90,380,15,40],
])

bestProds=np.max(prods.T,axis=1)  #最牛逼商品

prods_new = pd.DataFrame(prods,
                    columns = ['sales', 'clicks', 'reviews', 'favs'],
                    index = [101, 102, 103, 104,105])
def set_dist(row):
    return
#prods_new['dist']=prods_new.apply(set_dist,axis=1)
prods_new['dist']=prods_new.apply(lambda row:distance.cdist(np.array([row]),np.array([bestProds]),'euclidean')[0][0],axis=1)
print(prods_new.sort_values(by='dist',ascending=False))
#4,1,5,3,2

