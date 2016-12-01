import numpy as np

array1 = np.arange(15).reshape(3, 5)

rank = array1.ndim

shape = array1.shape

a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a - b
d = 10 * np.sign(a)
e = a < 35

f = np.random.random((2, 3))

time = np.linspace(20, 145, 5)
data = np.sin(np.arange(20)).reshape(5, 4)
ind = data.argmax(axis=0)
time_max = time[ind]
data_max = data[ind, range(data.shape[1])]

import matplotlib.pyplot as plt

mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
plt.hist(v, bins=50, normed=1)
plt.show()
