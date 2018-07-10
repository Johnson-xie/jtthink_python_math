import  numpy as np
import  pandas as pd

 # 1 表示
 # 2 取值 切片
sales=np.array([23,40,55,62,30,29])


ss=pd.Series(sales,index=[101,102,104,103,105,106])
#
# print(ss.sort_index(ascending=False)) #asc #desc

print(ss.sort_values(ascending=False))



