import pandas as pd
import numpy as numpy
#===merge two dataframe===
arr1 = pd.DataFrame({
    "employee_Id":[1,2,3,4],
    "salary":[120000,130000,105000,120000],
    "name":["bhawani","bhuvan","divyansh","akalvya"]
})
arr2 = pd.DataFrame({
     "employee_Id":[1,2,3,4],
        "sex":["male","male","male","male",],
        "address":["hp" , "panjab","panjab","jammu" ]
})
# print(arr1.shape)
# print(arr2.shape)
# print(pd.merge(arr1,arr2))

#===concatination of dataframe===

arr11 = pd.DataFrame({
    'a': ["a0","a1","a2"],
    'b': ["b0","b1","b2"],
    'c': ["c0","c1","c2"],
})
arr22 = pd.DataFrame({
    'a': ["a3","a4","a5"],
    'b': ["b3","b4","b5"],
    'c': ["c3","c4","c5"]
})
# print(pd.concat([arr11,arr22]))
# print(pd.concat([arr11,arr22],axis = 1))

#===joining dataframe===

arr3 = pd.DataFrame({
    "name":["bhawani","bhuvan","divyansh","akalvya"]
},index = [1,2,3,4]
)
arr4 = pd.DataFrame({
    "salary":[120000,130000,105000,120000],
},index = [1,3,4,5]
)
print(arr3.join(arr4))