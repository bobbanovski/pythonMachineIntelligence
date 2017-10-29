import numpy as np

#matrix - 2D numpy array
#vector - 1D numpy array

M = np.array( [ [1,2],[3,4] ] )

L = [ [1,2], [3,4] ]

#Retrieve data

print("List")
print(L[0])
print(L[0][0])
print(L)

print("Matrix")
print(M[0])
print(M[0][0])
print(M[0,0])
print(M)

#Convert matrix to array
A = np.array(M)
print(A)
#Transpose of array
print(A.T)

#Generate matrix
print("zeros array")
Z = np.zeros(10)
print(Z)
print("zeros matrix")
ZM = np.zeros( (10,10) ) #input tuple with each dimension
print(ZM)
print("Ones array")
O = np.ones( (10,10) )
print(O)

print("Random array size 10")
R = np.random.random( (10, 10) )
print(R)

print("Create Gaussian normal probability distribution matrix")
#needs integers not tuple
G = np.random.randn(10,10)
print(G)

print(G.mean())
print(G.var())