import numpy as np

# 余弦定理:参考 https://baike.baidu.com/item/%E4%BD%99%E5%BC%A6%E5%AE%9A%E7

# 向量 x
# 向量的长度，在多维中叫范数（线性代数概念）
# L1范数：x各个元素绝对值之和
# L2范数：x各个元素平方和的1/2次方（平方根），欧几里得范数
# Lp范数：||x|| 为x各个元素绝对值p次方的1/p次方
# L∞范数：||x|| 为x各个元素绝对值最大那个元素的绝对值

# linagl包，各种线性代数函数
# 它是linear(线性)和algebra(代数)的缩写,其中范数的英文是norm

v1 = np.array([5, 4, 4, 1, 4, 2])

print(np.linalg.norm(v1))  # ord参数来控制到底是几范数 ,默认是2

# 完整代码
v1 = np.array([5, 4, 4, 1, 4, 2])
v2 = np.array([2, 2, 5, 3, 5, 2])
print(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
