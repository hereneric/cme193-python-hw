count = 0
x = 11
while count < 20:
    if x % 5 == 0 and x % 7 == 0 and x % 11 == 0:
    	print x
    	count = count + 1
    x = x + 1