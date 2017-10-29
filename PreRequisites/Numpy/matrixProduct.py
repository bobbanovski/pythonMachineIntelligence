import numpy as np

# C = sum( A x B )
# C = A.dot(B) - matrix multiplication

# C = A * B - this is element wise multiplication
print("Matrix inverse")
A = np.array( [ [1,2],[3,4] ])
Ainv = np.linalg.inv(A)
print(A)
print(Ainv)
print("Identity")
print(Ainv.dot(A))

print("determinant")
print(np.linalg.det(A))

print("diagonal")
print(np.diag(A))
print(np.diag([1,2])) #pass in 1D get 2D back

print("Outer Product")
#Sum = E(x - mu)(x-mu)^T
#    1     sum(x - xmean)(x - xmean)^T
#   N - 1     (         )(         )
#C = sum over

a = np.array([1,2])
b = np.array([3,4])
print(np.outer(a,b))

print("Inner Product")
print(np.inner(a,b))
print(a.dot(b))

print("Matrix trace - sum of diagonals")
print(np.diag(A).sum())
print(np.trace(A))