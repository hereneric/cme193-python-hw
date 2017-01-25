def divisible_by_all(x):
    for i in range(1, 11):
        if x % i != 0:
            return False
    return True

x = 1
while divisible_by_all(x) == False:
    x = x + 1
print x