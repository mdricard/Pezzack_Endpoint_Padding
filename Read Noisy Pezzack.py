import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('d:/Noise_Pezzack.csv', delimiter=',', skip_header=1)
x = data[:, 0]
y = data[:, 1]
plt.plot(y)
plt.show()

