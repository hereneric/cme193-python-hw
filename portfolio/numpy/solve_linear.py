import numpy as np
from scipy.linalg import toeplitz

n = 200
m = 500
B = toeplitz(np.random.randn(1,m))
b = np.random.randn(m,1)

x = np.linalg.solve(B, b)
print x