import  pandas as pd

users_info=pd.read_csv("./files/users-info.csv",index_col=0)
users_score=pd.read_csv("./files/users-score-uname.csv",index_col=0)



print(users_info.join(users_score.groupby(['username']).sum(),how='inner',on='username'))

#groupy sum

