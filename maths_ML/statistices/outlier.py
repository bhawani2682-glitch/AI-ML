import numpy as np
import pandas as pd

arr = np.array([10,12,13,15,17,18,19,25,25,35,101])
q1=np.percentile(arr,25)
q2 = np.median(arr)
q3=np.percentile(arr,75)

iqr = q3-q1
print(iqr)
upper = q3 + 1.5(iqr)
lower = q1 - 1.5(iqr)

list = []
for i in arr:
    if i>=lower and i<=upper:
        list.append
print(i)        