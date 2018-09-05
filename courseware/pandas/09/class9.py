import  pandas as pd

#users=pd.read_csv("./files/class9/users.csv",index_col=[0,1])
#print(users.loc[103].loc['C罗'])
#print(users[(users['username']=='C罗') & (users.index==103)])

prods=pd.read_csv("./files/class9/prods.csv",index_col=[2,3])
prods_month=prods.sort_index()

idx=pd.IndexSlice

#print(prods_month.loc[(slice(3,4),slice(11,21)),:])

print(prods_month.loc[idx[:,11:21],:])


