import numpy as np
from sklearn.linear_model import LinearRegression

m = 5
n = 3
A = np.random.rand(m, n)
b = np.random.rand(m, 1)
lm = LinearRegression()
# scipy linear regression
lm.fit(A, b)
print lm.residues_