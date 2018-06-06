import  numpy as np

A=np.array([100,150,200,90,110])  # 130


B=np.array([140,120,130,150,110])  #130


# print(B.var()) #方差
# print(B.std()) #标准差

print(np.square(A-A.mean()).sum()/(A.size-1))
print(A.var())






