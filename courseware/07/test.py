import numpy as np

# 矩阵加/减
# 同行同列

m1 = np.array([[150, 10, 25],
               [200, 20, 20],
               [400, 15, 10]])

m2 = np.array([[250, 20, 15],
               [100, 12, 5],
               [300, 13, 20]
               ])

print(m1 + m2)
print(np.matrix(m1) + np.matrix(m2))
# 每一项的==
print(m1 == m2)

# m1.shape (行，列)
rows = m1.shape[0] - m2.shape[0]

# 函数np.insert
# 文档在此:https://docs.scipy.org/doc/numpy/reference/generated/numpy.insert.html

# m1 = np.insert(m1, 1, [[0, 0, 0]], axis=0)

# 第一个参数是源数组(矩阵 )
# 第二个参数是索引
# 第三个参数值插入的值（维度要和原数组一致）
# 第四个参数:axis=0 代表插入行，=1代表插入列

# numpy.zeros函数，来构建一个全0的数组（矩阵）
# 文档:https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.zeros.html
zero_rows = np.zeros((1, 3), int)  # 构建一个一行3列的矩阵，int型
print(zero_rows)


m1 = np.array([[150, 10, 25],
               [200, 20, 20],
               [400, 15, 10]])

m2 = np.array([[250, 20, 15],
               [100, 12, 5],
               [300, 13, 20],
               [300, 13, 20]
               ])
zero_rows = np.zeros((m2.shape[0] - m1.shape[0], m2.shape[1]), int)
m1 = np.insert(m1, m1.shape[0], zero_rows, axis=0)
print(m1)




