import time
import numpy as np
"""
q2(2): fibonacci sequence

Explanation
Naive recursive function is far slower than non-recursive/iterative
function, it is because the recursion works by performing depth
first search. Many intermediate results are recomputed many times.
But non-recursive function is one pass through the n numbers, and
it is O(n) time. Improved recursive solution saves intermediate values
in a dictionary and thus reduce computation time by a large scale.
"""
def fibo_recur(n):
	"""
	recursively compute fibonacci sequence
	slowest way
	"""
	if n < 1:
		return 0
	elif n == 1:
		return 1
	else:
		# sum of previous two numbers
		return fibo_recur(n-1) + fibo_recur(n-2)

def fibo_nonrecur(n):
	"""
	iteratively compute fibonacci sequence
	fast
	"""
	if n < 1:
		return 0
	elif n == 1:
		return 1
	prev = 1
	prev_prev = 0
	# compute from the first one
	for i in xrange(1, n):
		curr = prev + prev_prev
		prev_prev = prev
		prev = curr
	return curr

def fibo_recur_improved(n):
	"""
	recursive solution with intermediate results saved in dictionary
	quite fast
	"""
	dic = {}
	dic[0] = 0
	dic[1] = 1
	def helper(x):
		"""
		helper function to do recursion
		"""
		if x < 1:
			return 0
		elif x == 1:
			return 1
		else:
			# check if x-1 and x-2 are already in dictionary
			# use cached values if there
			if x-1 in dic:
				prev = dic[x-1]
			else:
				prev = helper(x-1)
			if x-2 in dic:
				prev_prev = dic[x-2]
			else:
				prev_prev = helper(x-2)
			result = prev + prev_prev
			if x not in dic:
				# save x into dictionary if not present
				dic[x] = result
			return result
	return helper(n)

def test_fibo():
	a = range(5)
	ans1 = map(lambda x: fibo_recur(x), a)
	ans2 = map(lambda x: fibo_nonrecur(x), a)
	ans3 = map(lambda x: fibo_recur_improved(x), a)
	assert np.array_equal(ans1, np.asarray([0, 1, 1, 2, 3]))
	assert np.array_equal(ans2, np.asarray([0, 1, 1, 2, 3]))
	assert np.array_equal(ans3, np.asarray([0, 1, 1, 2, 3]))

test_fibo()
t1 = time.time()
num1 = fibo_recur(35)
t2 = time.time()
print "Naive recursion takes %f seconds" % (t2 - t1)
t3 = time.time()
num2 = fibo_nonrecur(35)
t4 = time.time()
print "Iterative solution takes %f seconds" % (t4 - t3)
t5 = time.time()
num3 = fibo_recur_improved(35)
t6 = time.time()
print "Improved recursion takes %f seconds" % (t6 - t5)