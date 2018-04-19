import numpy as np


# 1、mean : 就是算术平均数  (也是我们和我们理解的均值)
# 2、median:中位数(将数据按大小顺序排列起来，形成一个数列，居于数列中间位置的那个数据)，等差数列中，中位数和平均数是相等的
# 3、mode:众数 也就是出现最多的数

arr = np.array([1,3,5,7,9])

# 平均数
print(arr.mean())
print(np.mean(arr))


# 比如工资
arr_salary = np.array([1000,1500,800,2000,900,1200,20000,0])
print(np.mean(arr_salary))
print(np.median(arr_salary))

# 修改数组维度
arr = np.array([1,3,5,7,9,9])
arr.shape = (2,3) # 2*3 必须=元素个数
print(arr)
# arr.reshape(2,3)

# 简单排序
# print(arr_salary.sort())
print(np.sort(arr_salary))

