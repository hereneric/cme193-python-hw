for x in range(2, 21):
    output = ''
    for i in range(2, x):
        if x % i == 0:
            output = output + str(i) + ' '
    print "For " + str(x) + " the output: " + output
