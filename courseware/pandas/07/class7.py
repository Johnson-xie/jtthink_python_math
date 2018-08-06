import  pandas as pd

users_info=pd.read_csv("./files/users-info.csv",index_col=0)
users_score=pd.read_csv("./files/users-score-uname2.csv",index_col=0)
print(users_info.reset_index())
print(users_info.reset_index().merge(users_score,left_on="username",right_on="userlogin").set_index("userid"))




