def primes(n):
	"""
	find primes within 2 lines of code
	"""
	is_prime = lambda x : len([i for i in range(2, x) if x % i == 0]) == 0
	return [i for i in range(2, n) if is_prime(i)]

print primes(100)