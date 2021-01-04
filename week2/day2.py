#importing numpy module
import numpy as np
from numpy import random
import math

#numpy version
print(np.__version__)

#task1
samplelist = [1,2,3,4,5]
samplelist.sort(reverse = True)
for i in range(len(samplelist)):
    samplelist[i] = float(samplelist[i])

arr = np.array(samplelist)
print(arr)
print("\n")

#task2
random_matrix = random.randint(100, size=(4,3))
print('Original matrix')
print(random_matrix )
print("\n")
print('Reshaped matrix:')
reshaped_matrix = random_matrix.reshape(2,6)    #reshaped matrix
print(reshaped_matrix)

#task3
mat1 = random.randint(50, size=(3,5))
mat2 = random.randint(50, size=(7,5))
print("\n Matrix 1:-")
print(mat1)
print("\n Matrix 2:-")
print(mat2)
#join matrix
join_mat = np.concatenate((mat1,mat2))
print("\n Concatenated matrix along axis 0:-")
print(join_mat)
print(f"\n Shape of concatenated array is: {np.shape(join_mat)}")

#task4
mat3 = random.randint(10, size=(3,3))
mat4 = random.randint(10, size=(3,3))
print("\n Matrix 1:-")
print(mat3)
print("\n Matrix 2:-")
print(mat4)
#inner product
inner_prod = np.inner(mat3, mat4)
#outer product
outer_prod = np.outer(mat3, mat4)
print(f"\n Inner product of 2 matrices is :- \n {inner_prod}")
print(f"\n Outer product of 2 matrices is :- \n{outer_prod}")

#task5
arr1 = np.array(random.randint(10,size=8))
print(f'\n1-D array is {arr1}')
print(f'\nReverse of arr1 is:- {arr1[::-1]}')

#task6
M = random.randint(10, size=(2,3))
print(f'\nMatrix M is :- \n{M}')
N = []
for row in range(2):
    for col in range(3):
        if row%2!=0 and col%2==0:
            N.append(M[row,col])
print(f'\nMatrix N is: {N}')

#task7
mat = np.arange(25, dtype=float).reshape(5,5)
print(f'\nTask 7 Matrix is: \n{mat}')
del_mat = np.delete(mat,1,0)
print(f'\nAfter deleted 2nd row: \n{del_mat}')
new_mat = np.insert(del_mat,1,np.nan,0)
print(f'\nNew matrix after inserting NAN values: \n{new_mat}')

#task8
a = np.arange(9).reshape(3,3)
print(f'\nOriginal matrix: \n{a}')
sum_of_rows = a.sum(axis=1)
#print(sum_of_rows)     array containing each row sum
#print(sum_of_rows[:,np.newaxis])      
normalized_arr = a/sum_of_rows[:,np.newaxis]
print(f'\nNormalized form of matrix is: \n{normalized_arr}')