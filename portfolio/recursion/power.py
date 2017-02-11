def power(a, b):
	a = float(a)
	if b == 0:
		return 1
	elif b < 0:
		return power(a, b+1) / a
	else:
		return power(a, b-1) * a

print power(2, 3)
print power(2, 0)
print power(2, -3)
print power(1.1, 2)