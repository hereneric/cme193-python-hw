import random

def generate(n, a, b, filename):
    """
    Generate random numbers and write to file
    """
    with open(filename, 'w') as f:
        for i in xrange(n):
            f.write(str(random.randint(a, b)) + '\n')
    f.close()

def read(filename):
    l = []
    with open(filename, 'r') as f:
        for line in f:
            l.append(int(line))
    f.close()
    return l

generate(2000, 1, 10000, 'integers1.txt')
generate(2000, 1, 10000, 'integers2.txt')
l1 = read('integers1.txt')
l2 = read('integers2.txt')
k = 12000
num_set = set()
for num in l1:
    num_set.add(num)

for num in l2:
    if k - num in num_set:
        print str(k - num) + ' ' + str(num)
