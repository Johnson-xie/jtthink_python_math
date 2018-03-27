import numpy as np

# 行向量
# 列向量
arr = np.array([1,2,3,4,5])
print(arr)
print(arr.T)

arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr1.T)


#
v1=np.array([2,4])
v2=np.array([3,4])

v3=np.array([[2,4]])
v4=np.array([[3,4]])

# 向量的点积/矩阵的点积
print(np.dot(v1,v2))
print(np.vdot(v3,v4))

# π
print(np.pi)

# 矩阵/array
arr = np.array([[2,3,4],[3,3,2]])
# matrix = np.matrix([[2,3,4],[3,3,2]])
matrix = np.matrix(arr)
matrix2 = np.matrix("2,3,4;3,3,2")
print(arr)
print(matrix)
print(matrix2)

# np.matrix / np.mat
# 看文档
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.mat.html
arr=np.array ([[1,2],[3,4]])

mat1 = np.matrix(arr)
mat2 = np.mat(arr)

# 如果我去更改 arr的某个值
arr[0][0]=5

print(mat1)
print(mat2)
# matrix对原对象进行了一份拷贝。修改原值无影响，则mat则有影响
