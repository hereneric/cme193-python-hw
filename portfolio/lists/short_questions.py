def print_list(l):
    for element in l:
        print element

def print_list_reverse(l):
    for element in reversed(l):
        print element

def len_list(l):
    count = 0
    for element in l:
        count += 1
    return count

l = [1, 2, 3]
print_list(l)
print_list_reverse(l)
print len_list(l)
