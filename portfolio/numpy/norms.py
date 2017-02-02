import numpy as np
from scipy.linalg import toeplitz

n = 200
m = 500
B = toeplitz(np.random.randn(1,m))

print np.linalg.norm(B, 2)
print np.linalg.norm(B, np.inf)
print np.linalg.norm(B, -2)