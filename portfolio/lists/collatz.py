def collatz(x):
    """
    return a list of collatz sequence
    """
    sequence = []
    while x != 1:
	    sequence.append(x)
	    if x % 2 == 0:
	    	x = x / 2
	    else:
	    	x = 3 * x + 1
    sequence.append(1)
    return sequence

def find_longest(x):
    """
    Find the longest collatz sequence in numbers 1 to x
    """
    max_len = -1
    result = -1
    for i in xrange(1, x):
        length = len(collatz(i))
        if length > max_len:
            max_len = length
            result = i
    return result

print collatz(837799)
print find_longest(1000000)