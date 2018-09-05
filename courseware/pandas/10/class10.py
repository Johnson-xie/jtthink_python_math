import  pandas as pd
import numpy as np




prods_rep=pd.DataFrame(np.random.randint(1000,10000,size=(31,3))
                       ,columns=['图书类','生活用品','母婴用品']
                       ,index=pd.date_range('2018-1-1',periods=31,freq="D"))

print(prods_rep)
prods_rep.to_csv("./files/class10/prods_rep.csv",index_label="日期")

