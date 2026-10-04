from numpy import *
A = array([[1,2,3],[4,5,6],[7,8,9]])#martix A#
B = array([
    [9,8,7],
    [6,5,4],
    [4,3,2],
    [1,4,3]]
)

print(B.shape) # to give the shape of the matrix(rows, columns)
print(A.ndim)# to give the dimension of the matrix
print(A.size)#to find the total number of elements
print(A.dtype)#to find the data type of the array
print(B)

# print(A+B)# to add of the matrix
# print(A - B)#to subtract of the matrix
# print(A@B)#to multiply of the matrix
# print(A.T)# to transpose the matrix
# print(linalg.det(A))# to determinant of the matrix
# print(linalg.inv(A))# to inverse of the matrix
# print(linalg.trace(A))# to trace of the matrix
# print(linalg.matrix_rank(A))#to find the rank of the matrix
# print(linalg.eig(A))# to find the eigen value and eigen vector of the matrix