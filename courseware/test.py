import numpy as np

arr = np.array([
    [1, 2 ,3],
    [2, 3, 4]
])

insert_arr = [
    [0, 0, 0],
    [0, 0, 0],
]

result = np.insert(arr, 1, insert_arr, axis=0)
print(result)