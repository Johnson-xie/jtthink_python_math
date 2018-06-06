import  numpy as np

A=np.array([100,150,200,90,110])  # 130


B=np.array([90,80,60,150,95])  #95


print(np.sum((A-A.mean())*(B-B.mean()))/4)


print(np.var(A,ddof=1))  #样本方差
print(np.cov(A))  #协方差
print(np.var(B,ddof=1))
print(np.cov(A,B))