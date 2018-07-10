import numpy as np
import pandas as pd



# sales=pd.read_csv("./files/p1.txt",squeeze=True)
# print(sales)
# print(type(sales))

# sales=pd.read_csv("./files/p2.txt",squeeze=True,index_col=0,header=None)
# print(sales)
# print(type(sales))


sales=pd.read_csv("./files/p3.txt",squeeze=True,index_col=0)
print(sales.mean())
print(sales[sales>=sales.mean()])
print(sales[sales<sales.mean()].index.tolist())

print(sales[sales>=sales.mean()].sum()-sales[sales<sales.mean()].sum())