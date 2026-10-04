import numpy as np
import time
# n =  10000000   #vector adddition in both numpy and python loop
# a = [1]*n
# b = [2]*n        
# start = time.time()

# c  = [0]* n   
# for i in range(n):#python loop
#     c[i] = a[i] + b[i]
# end = time.time()
# py = end - start
# print(py)    


# a_np = np.arange(n)
# b_np = np.arange(n)

# c_np = a_np + b_np
# ny = end - start
# print(ny)
# print(py//ny)

######time effiency for array_numpy and py_list
py_list = [1,2,3]
num = np.array([1,2,3])

start = time.time()
py_list = [i* 2 for i in range(100000)]
num = np.arange(100000) * 2
print(time.time()- start)
print(time.time()- start)