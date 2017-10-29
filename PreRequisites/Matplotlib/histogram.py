import matplotlib.pyplot as plt
import numpy as np

# A = pd.read_csv('data_1d.csv', header=None).as_matrix()
# x = A[:,0]
# y = A[:,1]
R = np.random.random(10000)

plt.hist(R, bins = 20)
plt.show()