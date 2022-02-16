from timeit import timeit

# List
result = timeit(setup="num_list = [x for x in range(0,10000)]", stmt="for i in num_list: z = i", number=10000)
print(result)

# array.array
result = timeit(setup="from array import array; num_array = array('i', [x for x in range(0,10000)])", stmt="for i in num_array: z = i", number=10000)
print(result)

#numpy 
result = timeit(setup="import numpy as np; np_array = np.array([x for x in range(0,10000)])", stmt="for i in np_array: z = i", number=10000)
print(result)