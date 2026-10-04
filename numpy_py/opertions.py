#Importing NUMpy in to the program
import numpy as np
#Creating an array
arr1 = np.array([1,2,3,4,5,6,7,8,9],dtype ="int32")

# Important fanction of NUMpy for ML
print(arr1.dtype)#to get the data type of the array
print(arr1.shape)#to get the number of rows and columns in the array
print(arr1.size)#to get the total number of elements
print(np.zero(3,4))#to get a array filed with zero
print(np.one(3,4))#o get a array filed with one
print(np.full(8))#o get a array filed with a specific value
print(np.empty(5))#to create a array without initializing it 
print(np.range(1,10,2))#to get a number of elements in a range(start , end , difference)
print(np.linspace(5,50,4))#output = [5 , 20, 35,50]
print(np.eye(3,4))#to create a indentity matrix
print(np.arange(10).reshape(3,4))#to reshape a array(in rows and columns)
print(np.arange(10).flatten())#to rashape a array(In flatten)
print(np.arange(10).reshape(2,2).reval())#to convert a array into a 1-d array
print(np.arr.T)#to get the array transpose
print(np.concatenate(arr1))#joins arrays verticaly along the existing axis
print(np.sort(arr1))#to get a sort in the array in ascending  order