import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100) #start, stop, number of points in between

#create sin wave
y = np.sin(x)

plt.plot(x,y)
plt.xlabel("Time")
plt.ylabel("Function of Time")
plt.title("Sine Wave")
plt.show()