def arith1(x):
  """ Given an integer number x, returns:
      0, if x is negative or 0
      x, if x is strictly positve and less than or equal to 10
      10, otherwise """    
  
  if x <= 0:
    return 0
  elif x <= 10:
    return x

  return 10

def arith2(x, y):
  """ Given two integer numbers x and y, returns:
      
      2x + y, if x is strictly greater than y
      4y - 3, if y is strictly greater than x
      x^3 + xy, if x is equal to y """
  if x > y:
    return 2 * x + y
  elif y > x:
    return 4 * y - 3
  else:
    return x ** 3 + x * y

def arith3(x, y, z):
  """ Given three integer numbers x, y, and z, returns:
      
      0, if any of the two numbers are the same
      1, if the numbers are ordered such that x < y and y < z
      2, otherwise """
  if x == y or y == z or z == x:
    return 0
  elif x < y and y < z:
    return 1
  else:
    return 2

def arith4(x, y, z, w):
  """ Given four integer numbers x, y, z, and w, returns:
 
      the maximum of arith2(x, y) and arith2(z, w), if x is strictly less than y
      the sum of arith3(z, y, x) and arith1(w), otherwise """
  if x < y:
    return max(arith2(x, y), arith2(z, w))
  else:
    return arith3(z, y, x) + arith1(w)
