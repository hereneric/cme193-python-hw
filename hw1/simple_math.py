def seq_add(start, end, k):
  """ Returns the sum of every k-th number between start and end. For example:
      seq_add(1, 10, 3) returns 1 + 4 + 7 + 10 = 22
      seq_add(1, 11, 3) returns 1 + 4 + 7 + 10 = 22
      seq_add(1, 5, 6) returns 1
      seq_add(4, 9, 2) returns 4 + 6 + 8 = 18 
      seq_add(7, 7, 3) returns 7
      seq_add(-4, 8, 5) returns -4 + 1 + 6 = 3

      You can assume start <= end and that k > 0 """
  result = 0
  for i in range(start, end + 1, k):
    result += i
  return result

def fact(n):
  """ Returns n!, the factorial of n.  If n <= 0, return 0.  For example:
      fact(5) returns 5 * 4 * 3 * 2 * 1 = 120
      fact(-2) returns 0

      You can assume that n is an integer.

      You are not allowed to use Python's math library.  """
  factorial = 1
  if n > 0:
    for i in xrange(1, n + 1):
      factorial *= i
    return factorial
  return 0
