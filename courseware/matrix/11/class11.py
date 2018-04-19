import  numpy as np
works=np.array([[150,10],
                [200,20]
             ])
money=np.array([[170],
                [240]
             ])  #2*1
# fee=np.array([[1],
#               [2]])

works_inv=np.linalg.inv(works)  #2*2  *   2*1

fee=np.dot(works_inv,money)
print(fee)
