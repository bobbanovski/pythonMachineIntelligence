import numpy as np

#Ax = b
#A^-1 Ax = A^-1 b

A = np.array([ [1,2],[3,4] ])
print(A)
b = np.array([1,2])
x = np.linalg.inv(A).dot(b)
print(x)

#Quicker
print("Solver")
x = np.linalg.solve(A, b)
print(x)

#Word problem
A = np.array([ [1, 1], [1.5, 4] ])
b = np.array([2200, 5050])
x = np.linalg.solve(A, b)
print("Solution to word prob")
print(x)