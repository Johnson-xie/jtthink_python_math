import  numpy as np

works=np.array([[150,10],
                [250,20]
             ])

fee=np.array([[1],
              [2]])


print(np.dot(works,fee))

print(np.matrix(works)*np.matrix(fee))
