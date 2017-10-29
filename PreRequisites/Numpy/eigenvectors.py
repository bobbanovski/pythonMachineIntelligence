import numpy as np

#Create matrix with normally distributed values between 0, 1 (Gaussian)
#100 samples (Rows), 3 features (Columns)
X = np.random.randn(100,3)
print(X)

#covariance - use transpose to make 3x3 (# of columns)
print("covariance")
cov = np.cov(X.T)
print(cov)

#eigh - symmetric, Hermitian matrices
#Symmetric - A = A^T
#Hermitian - A = A^H
#A^H - conjugate transpose of A

C = np.linalg.eigh(cov)
print(C) #tuple - 3 eigenvalues, then eigenvectors
