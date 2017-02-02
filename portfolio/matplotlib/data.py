import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin

X = np.random.rand(20,10)
b = np.random.rand(10,1)
z = np.random.randn(20,1)
y = X.dot(b) + z
print y.shape

def f(x):
	return np.linalg.norm(X.dot(x) - y, 2)

x0 = np.random.rand(10,1)
b_opt = fmin(lambda x: f(x), x0)

line_up, = plt.plot(range(len(b)), b, 'rx')
line_down, = plt.plot(range(len(b)), b_opt, 'bo')
plt.xlabel('index')
plt.ylabel('value')
plt.legend([line_up, line_down], ['True Coeff', 'Estimated Coeff'])
plt.show()