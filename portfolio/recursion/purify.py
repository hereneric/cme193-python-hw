def purify_iteration(l):
	result = []
	for num in l:
		if num % 2 == 0:
			result.append(num)
	return result

def purify_recursion(l):
	length = len(l)
	result = []
	if length < 1:
		return []
	if length == 1:
		if l[0] % 2 == 0:
			result.append(l[0])
		return result
	l1 = l[:length/2]
	l2 = l[length/2:]
	l1_result = purify_recursion(l1)
	l2_result = purify_recursion(l2)
	result.extend(l1_result)
	result.extend(l2_result)
	return result

print purify_iteration([0,1,2,3,4,5,6,8,9,-2])
print purify_recursion([0,1,2,3,4,5,6,8,9,-2])