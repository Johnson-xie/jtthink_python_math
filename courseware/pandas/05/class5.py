import  pandas as pd
prods=pd.read_csv("./files/c3-prods.txt",index_col=0)
prods['销量排名']=prods.rank(method="dense")['商品销量']
print(prods)