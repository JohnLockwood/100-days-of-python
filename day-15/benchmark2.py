from timeit import timeit
import numpy as np

iterations = 500

def display(elapsed_time, message, rounding=3):
    print(f"{round(elapsed_time, rounding)} seconds -- {message}.")

result = timeit(setup="num_list = [n for n in range(0,256)] * 1000", 
                stmt="sum(num_list)", number=iterations)
display(result, "Python sum function on a list of numbers")

result = timeit(setup="l = [n for n in range(0,256)] * 1000; num_array = bytearray(l)", 
                stmt="sum(num_array)", number=iterations)
display(result, "Python sum function on a bytearray of numbers")

result = timeit(setup="import numpy as np; l = [n for n in range(0,256)] * 1000; np_array = np.array(l)", 
                stmt="sum(np_array)", number=iterations)
display(result, "Python sum function on a NumPy array", rounding=4)

result = timeit(setup="import numpy as np; l = [n for n in range(0,256)] * 1000; np_array = np.array(l)", 
                stmt="np_array.sum()", number=iterations)
display(result, "NumPy sum method on a NumPy array")