def print_dict(dic):
	"""
	print dictionary items
	"""
	for key, val in dic.iteritems():
		print key, val

print_dict({'a':1, 'b':2})