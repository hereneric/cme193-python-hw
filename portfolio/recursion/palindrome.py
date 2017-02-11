def _identity_matrix(length):
	"""
	return an identity matrix of size length^2
	"""
	table = []
	for i in xrange(length):
		row = []
		for j in xrange(length):
			if i != j:
				row.append(0)
			else:
				row.append(1)
		table.append(row)
	return table

def palindrome(string):
	"""
	Return the longest palindromic subsequence
	"""
	length = len(string)
	table = _identity_matrix(length)
	diff = 1
	maxlen = -1
	p = -1
	q = -1
	for p in xrange(2, length + 1):
		for i in xrange(length - p + 1):
			j = i + diff
			if string[i] == string[j]:
				table[i][j] = table[i+1][j-1]+2
			else:
				table[i][j] = max(table[i+1][j], table[i][j-1])
			if table[i][j] > maxlen:
				p = i
				q = j
		diff += 1
	result = ""
	print p,q
	while p != q:
		if table[p][q] == table[p][q-1]:
			q -= 1
		elif table[p][q] == table[p+1][q]:
			p += 1
		else:
			result = string[q] + result
			q -= 1
			p += 1
	return result[::-1] + string[q] + result

print palindrome('abcdcba')