import math

'''
Convert a tuple of spherical coordinates to a tuple of cylindrical coordinates.

coords is a tuple in (r, theta, phi) form
return value is a tuple in (rho, phi, z) form
'''
def sphere2cyl(coords):
  return cart2cyl(sphere2cart(coords))

'''
Convert a tuple of spherical coordinates to a tuple of cartesian coordinates.

coords is a tuple in (r, theta, phi) form
return value is a tuple in (x, y, z) form
'''
def sphere2cart(coords):
  r, theta, phi = coords
  x = r * math.sin(theta) * math.cos(phi)
  y = r * math.sin(theta) * math.sin(phi)
  z = r * math.cos(theta)
  return (x, y, z)

'''
Convert a tuple of cylindrical coordinates to a tuple of spherical coordinates.

coords is a tuple in (rho, phi, z) form
return value is a tuple in (r, theta, phi) form
'''
def cyl2sphere(coords):
  return cart2sphere(cyl2cart(coords))


'''
Convert a tuple of cylindrical coordinates to a tuple of spherical coordinates.

coords is a tuple in (rho, phi, z) form
return value is a tuple in (x, y, z) form
'''
def cyl2cart(coords):
  rho, phi, z = coords
  x = rho * math.cos(phi)
  y = rho * math.sin(phi)
  return (x, y, z)


'''
Convert a tuple of cartesian coordinates to a tuple of spherical coordinates.

coords is a tuple in (x, y, z) form
return value is a tuple in (r, theta, phi) form
'''
def cart2sphere(coords):
  # From lecture 2 slides
  x, y, z = coords
  r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
  theta = math.acos(z / r)
  phi = math.atan2(y, x)
  return (r, theta, phi)


'''
Convert a tuple of cartesian coordinates to a tuple of cylindrical coordinates.

coords is a tuple in (x, y, z) form
return value is a tuple in (rho, phi, z) form
'''
def cart2cyl(coords):
  x, y, z = coords
  rho = math.sqrt(x ** 2 + y ** 2)
  phi = math.atan2(y, x)
  return (rho, phi, z)

'''
Convert a new list of points from one type to another

points is a list of tuples of points
type is the type of points in the list.  type is one of 'cart', 'sphere', 'cyl'
new_type is the type of 
'''
def convert_points(points, type='cart', new_type='cart'):
  if type is new_type:
    # Create a copy instead of returning the exact list
    return points[:]
  return eval('map(' + type + '2' + new_type + ', points)')
