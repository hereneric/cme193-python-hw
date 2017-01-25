def str1(a):
  """ Given a string a, returns the string aaa """
  return a * 3

def str2(a, b):
  """ Given strings a and b, returns the string abbba """
  return a + b * 3 + a

def str3(a, b, c):
  """ Given strings a, b, and c, returns the string abcabc """
  return (a + b + c) * 2

def str4(a, b, c, d):
  """ Given strings a, b, c, and d, returns:
      ab, if c and d are of the same length
      bbcc, otherwise   """
  if len(c) == len(d):
    return a + b
  return b * 2 + c * 2
