def product_iteration(l):
	result = 1.0
	for num in l:
		result *= num
	return result

def product_recursion(l):
	length = len(l)
	result = 1.0
	if length < 1:
		return 1.0
	if length == 1:
		return l[0]
	l1 = l[:length/2]
	l2 = l[length/2:]
	l1_result = product_recursion(l1)
	l2_result = product_recursion(l2)
	result *= l1_result
	result *= l2_result
	return result

print product_iteration([1,2,3,4,5,6,0.001,9,-2])
print product_recursion([1,2,3,4,5,6,0.001,9,-2])