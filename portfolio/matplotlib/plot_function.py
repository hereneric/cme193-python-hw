import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return ((np.sin(x-2)) ** 2) * np.exp(-x ** 2)

x = np.arange(0, 2, 0.01);
y = f(x)

plt.plot(x, y)
plt.ylabel('y')
plt.xlabel('x')
plt.title('plot function')
plt.show()