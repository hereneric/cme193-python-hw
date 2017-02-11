import time

def fibo_recur(n):
	if n < 1:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo_recur(n-1) + fibo_recur(n-2)

def fibo_nonrecur(n):
	if n < 1:
		return 0
	elif n == 1:
		return 1
	prev = 1
	prev_prev = 0
	for i in xrange(1, n):
		curr = prev + prev_prev
		prev_prev = prev
		prev = curr
	return curr

def fibo_recur_improved(n):
	dic = {}
	dic[0] = 0
	dic[1] = 1
	def helper(x):
		if x < 1:
			return 0
		elif x == 1:
			return 1
		else:
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
				dic[x] = result
			return result
	return helper(n)

a = range(30)
print map(lambda x: fibo_recur(x), a)
print map(lambda x: fibo_nonrecur(x), a)
print map(lambda x: fibo_recur_improved(x), a)
# Recursive function is far slower than non-recursive/iterative
# function, it is because the recursive one works by performing
# depth first search. Many intermediate results are recomputed
# many times. But non-recursive function is one pass through the
# n numbers, and it is O(n) time.
t1 = time.time()
num1 = fibo_recur(36)
t2 = time.time()
print t2 - t1
t3 = time.time()
num2 = fibo_nonrecur(36)
t4 = time.time()
print t4 - t3
t5 = time.time()
num3 = fibo_recur_improved(36)
t6 = time.time()
print t6 - t5