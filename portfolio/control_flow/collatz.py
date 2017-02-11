x = 103
sequence = []
while x != 1:
	# Run until x is 1
	sequence.append(str(x))
	if x % 2 == 0:
		x = x / 2
	else:
		x = 3 * x + 1
sequence.append('1')
print ' '.join(sequence)