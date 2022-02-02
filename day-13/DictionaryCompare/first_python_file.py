# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import numpy.typing as nptype
l = [x for x in range(1, 11)]
n1 = 5
n3 = 3/5
n4 = 3//5

np_arr = np.array([x for x in range(1, 11)])
message = "Hello world"
print(np_arr)
print(message)

def get_np_array():
    """Return a 4x2 numpy array"""
    arr = np.arange(8.).reshape(4,2)
    return arr

def documented_fn():
    """I am some function documentation.  Let's see how I look in Sphinx!"""
    pass

np_arr3 = get_np_array()