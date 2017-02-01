from sklearn.linear_model import LinearRegression

class OLS:
	def __init__(self):
		self.lm = LinearRegression()

	def fit(self, X, Y):
		self.lm.fit(X, Y)

	def predict(self, x):
		"""
		x is an array where each row is an example
		"""
		return self.lm.predict(x)

	def summarize(self):
		print '='*20
		print 'The (coefficients, intercept) are as follows:'
		return (self.lm.coef_, self.lm.intercept_)
		print '='*20

ols = OLS()
X = [[1], [2], [3]]
Y = [1,3,5]
ols.fit(X,Y)
print ols.predict([[4],[5],[6]])
print ols.summarize()