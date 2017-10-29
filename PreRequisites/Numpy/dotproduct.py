import numpy as np

#dot function is an instance function of a numpy array -
#can use {numpyarray}.dot()
#dot product = a . b = |a| |b| cos(theta)
a = np.array([1,2])
b = np.array([2,1])

dot = 0
for e, f in zip(a,b):
    dot += e*f

#multiply 2 arrays together - arrays must be same size
print(a*b)

print(np.sum(a*b))
print(a*b.sum())
print("numpy dot product")
print(np.dot(a,b))
print(a.dot(b))
print(b.dot(a))

#calculate angle between a and b
print("angle between a and b")
print(np.sqrt(np.sum(a**2)))
print(np.sqrt(np.sum(b**2)))
#linalg module in numpy - magnitude
amag = np.linalg.norm(a)
bmag = np.linalg.norm(b)

cosangle = a.dot(b) / (amag*bmag)
print("cosanlge in radians")
print(np.arccos(cosangle))