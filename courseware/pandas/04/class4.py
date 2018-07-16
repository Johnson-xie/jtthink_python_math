import  pandas as pd


prods=pd.read_csv("./files/c3-prods.txt",index_col=0)


#prods['销售总额']=prods['商品销量']*prods['商品价格']
prods.insert(prods.columns.size,'销售总额',prods['商品销量']*prods['商品价格'])

# prods['销售情况']=''
# print(prods)
def time100(x):
    if x['销售总额'] >= prods['销售总额'].mean():
      return 'A级'
    return 'B级'

prods['销售情况']=prods.apply(lambda x:'A级' if x['销售总额'] >= prods['销售总额'].mean() else 'B级',axis=1)
print(prods['销售总额'].mean())
print(prods)
