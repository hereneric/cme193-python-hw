import math

'''
Convert a dictionary of spherical coordinates to a dictionary of
cylindrical coordinates.

coords is a dictionary with string keys 'r', 'theta', and 'phi' with
       corresponding values as spherical coordinate values
return value is a dictionary with keys 'rho', 'phi', and 'z'  with
       corresponding values as cylindrical coordinate values
'''
def sphere2cyl(coords):
  return cart2cyl(sphere2cart(coords))


'''
Convert a dictionary of spherical coordinates to a dictionary of
cartesian coordinates.

coords is a dictionary with string keys 'r', 'theta', and 'phi' with
       corresponding values as spherical coordinate values
return value is a dictionary with keys 'x', 'y', and 'z'  with
       corresponding values as cartesian coordinate values
'''
def sphere2cart(coords):
  r = coords['r']
  theta = coords['theta']
  phi = coords['phi']

  # initializing empty dictionary
  cart_points = {}

  cart_points['x'] = r * math.sin(theta) * math.cos(phi)
  cart_points['y'] = r * math.sin(theta) * math.sin(phi)
  cart_points['z'] = r * math.cos(theta)
  return cart_points


'''
Convert a dictionary of cylindrical coordinates to a dictionary of
spherical coordinates.

coords is a dictionary with string keys 'rho', 'phi', and 'z' with
       corresponding values as cylindrical coordinate values
return value is a dictionary with keys 'r', 'theta', and 'phi'  with
       corresponding values as spherical coordinate values
'''
def cyl2sphere(coords):
  return cart2sphere(cyl2cart(coords))


'''
Convert a dictionary of cylindrical coordinates to a dictionary of
cartesian coordinates.

coords is a dictionary with string keys 'rho', 'phi', and 'z' with
       corresponding values as cylindrical coordinate values
return value is a dictionary with keys 'x', 'y', and 'z'  with
       corresponding values as cartesian coordinate values
'''
def cyl2cart(coords):
  rho = coords['rho']
  phi = coords['phi']
  z = coords['z']

  # initializing empty dictionary
  cart_points = {}

  cart_points['x'] = rho * math.cos(phi)
  cart_points['y'] = rho * math.sin(phi)
  cart_points['z'] = z
  return cart_points

'''
Convert a dictionary of cartesian coordinates to a dictionary of
spherical coordinates.

coords is a dictionary with string keys 'x', 'y', and 'z' with
       corresponding values as cartesian coordinate values
return value is a dictionary with keys 'r', 'theta', and 'phi'  with
       corresponding values as spherical coordinate values
'''
def cart2sphere(coords):
  # From lecture 2 slides
  x = coords['x']
  y = coords['y']
  z = coords['z']

  # initialize empty dictionary
  cart_points = {}

  cart_points['r'] = math.sqrt(x ** 2 + y ** 2 + z ** 2)
  cart_points['theta'] = math.acos(z / cart_points['r'])
  cart_points['phi'] = math.atan2(y, x)

  return cart_points


'''
Convert a dictionary of cartesian coordinates to a dictionary of
cylindrical coordinates.

coords is a dictionary with string keys 'x', 'y', and 'z' with
       corresponding values as cartesian coordinate values
return value is a dictionary with keys 'rho', 'phi', and 'z'  with
       corresponding values as cylindrical coordinate values
'''
def cart2cyl(coords):
  x = coords['x']
  y = coords['y']
  z = coords['z']

  # initialize empty dictionary
  cyl_points = {}

  cyl_points['rho'] = math.sqrt(x ** 2 + y ** 2)
  cyl_points['phi'] = math.atan2(y, x)
  cyl_points['z'] = z
  return cyl_points

'''
Determine the type of the coordinate dictionary.

coords is a dictionary representing a point in either cartesian,
       spherical, or cylindrical coordinates
return value is a string of either 'cart', 'sphere', or 'cyl'

As an example:
  point1 = {'x': 1, 'y': 2, 'z': 3}
  point2 = cart2cyl(point1)
  print detect_type(point1) # should print 'cart'
  print detect_type(point2) # should print 'cyl'
'''
def detect_type(coords):
  keys = coords.keys()
  # detect type by checking the keys in the coords dict
  if 'x' in keys and 'y' in keys and 'z' in keys:
    return 'cart'
  elif 'r' in keys and 'theta' in keys and 'phi' in keys:
    return 'sphere'
  elif 'rho' in keys and 'phi' in keys and 'z' in keys:
    return 'cyl'
  return None
