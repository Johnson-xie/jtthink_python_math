import  numpy as np



def genMat(str,col=3):  #生成一个指定列为 col的矩阵
    if len(str)%col >0:
        str=str+(col-(len(str)%col))*" "
    str_list = list(map(lambda x: ord(x), str))
    return np.array(str_list).reshape(-1,3)

key_mat=None  #在外部定义一个秘钥矩阵 变量，后面要用

def genKey(n=3): #生成秘钥矩阵
    ret= np.random.randint(0, 2, (n, n))
    while(np.linalg.det(ret)==0):  #这里为了防止生成出 行列式为0的矩阵
        ret = np.random.randint(0, 2, (n, n))
    return ret


def encrypt(str,c=3): #加密
    clearText_mat=genMat(str,col=c)  #生成明文矩阵
    global key_mat
    key_mat=genKey(n=c)
    cipherText_mat=np.dot(clearText_mat,key_mat).reshape(-1,) #密文矩阵,使用reshape 把矩阵变成一维数组，方便等下变成密文
    cipherText="".join(list(map(lambda x: chr(x),cipherText_mat.astype(int))))  #chr把ascii转换成字符
    return cipherText

def decrypt(str,c=3):
    global key_mat
    cipherText_mat=genMat(str,col=c) #密文矩阵
    keyText_mat = np.linalg.inv(key_mat) #秘钥矩阵求逆
    clearText_mat=np.dot(cipherText_mat,keyText_mat).reshape(-1,) #明文矩阵，使用reshape 把矩阵变成一维数组
    clearText="".join(list(map(lambda x: chr(x),clearText_mat.astype(int))))
    return clearText

ret=encrypt("i am shenyi,hello python")
print(ret)
print(decrypt(ret))

