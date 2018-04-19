import numpy as np

users = ['zhang3', 'li4']
np_users = np.array(users)
# np_users.ndim 数组维度
# np_users.shape 数组行/列(2,3)
# np_users.dtype 元素的类型 （< 表示小端 ，>表示大端）
# np_users.itemsize 类型所占的字节数

print(type(users))      # <class 'list'>
print(users)            # ['zhang3', 'li4']
print(type(np_users))   # <class 'numpy.ndarray'>
print(np_users)         # ['zhang3' 'li4']

# 数组每项平方
arr = np.array([12,22,35,10])
print(np. square(arr))

# 指定加一定的数量（每一项相加）
plus = np.array([30,15,10,5])
print(arr+plus)
print(np.add(arr, plus))

# 数组求和
print(np.sum(arr))
print(arr.sum())

# 二维的，每一项求和
arr = np.array([[1,2],[3,4],[5,6]])
print(np.sum(arr, axis=1))
print(arr.sum())


