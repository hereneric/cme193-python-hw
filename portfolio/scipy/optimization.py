from scipy.optimize import fmin
import numpy as np

def f(x):
	return ((np.sin(x-2)) ** 2) * np.exp(-x ** 2)

max_x = fmin(lambda x: -f(x), 0)
print max_x