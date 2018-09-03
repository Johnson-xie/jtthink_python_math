import  pandas as pd

users1=pd.read_csv("./files/class8/users1.csv",index_col=0)
users2=pd.read_csv("./files/class8/users2.csv",index_col=0)



users=pd.concat([users1,users2],keys=["A","B"])

print(users.drop_duplicates("username"))



