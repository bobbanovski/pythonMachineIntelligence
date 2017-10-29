import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import pylab as pl

# A = pd.read_csv('data_1d.csv', header=None).as_matrix()
# x = A[:,0]
# y = A[:,1]
x_line = np.linspace(0,100, 100)
y_line = 2*x_line + 1

plt.plot(x_line,y_line)
plt.xlabel("Time")
plt.ylabel("Function of Time")
plt.title("data")
plt.show()