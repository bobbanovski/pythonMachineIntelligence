import numpy as np
L = [1,2,3]

A = np.array([1,2,3])

for element in L:
    print(element)
for element in A:
    print(element)
#equivalent actions to lists and numpy arrays

L.append(4)
#no equivalent append option for numpy array

L = L + [5]
#no equivalent append option for array

#vector addition
L2 = []
for element in L:
    L2.append(element + element)
print(2*L) #does not multiply - repeats
#Squaring a list
L2=[]
for element in L:
    L2.append(element*element)
print("list squaring")
print(L2)

#for numpy - matrix add and multiply,
print("Matrix addition and Multiplication")
matrixaddition = A+A
print(matrixaddition)
matrixmultiply = 3*A
print(matrixmultiply)
print("Matrix square")
print(A**2)

#Numpy commands on arrays
print("Numpy commands")
print("np.sqrt()")
print(np.sqrt(A))
print("np.log()")
print(np.log(A))
print("np.exp()")
print(np.exp(A))
