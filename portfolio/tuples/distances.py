def l1(tuple_x, tuple_y):
    sum = 0
    for i in range(len(tuple_x)):
        sum += abs(tuple_x[i] - tuple_y[i])
    return sum

def l2(tuple_x, tuple_y):
    sum = 0
    for i in range(len(tuple_x)):
        sum += (tuple_x[i] - tuple_y[i]) ** 2
    return sum

print l1((1,2,3), (0,0,0))
print l2((1,2,3), (0,0,0))
