import numpy as np

def get_array(size=10):
    return np.array([i for i in range(1,size + 1)])

arr = get_array()
print(arr)