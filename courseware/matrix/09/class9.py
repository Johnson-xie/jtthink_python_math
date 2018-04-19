import numpy as np

# 原始数据
news = np.array([[3, 5],
                 [2, 4],
                 [5, 2]
                 ])
# 矩阵 点积 矩阵的转置
news_dot_mat = np.dot(news, news.T)

# print(news_dot_mat)

# 模 矩阵
news_norm = np.linalg.norm(news, axis=1, keepdims=True)  # 模

news_norm_mat = np.dot(news_norm, news_norm.T) ** -1  # 模矩阵(倒数)

print(news_dot_mat * news_norm_mat)  # 广播 普通乘法

# sklearn 方式
# from sklearn.metrics.pairwise import cosine_similarity
# print(cosine_similarity(news))
