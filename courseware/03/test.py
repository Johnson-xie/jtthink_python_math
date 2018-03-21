import numpy as np

# 标准差
# - 1  样本标准差

arr = np.array([5, 9, 10])

# 根据公式计算
result = np.sqrt(np.sum(np.square(arr - np.mean(arr))) / (arr.size - 1))
print(result)

# np 直接计算
print(np.std(arr, ddof=1))
