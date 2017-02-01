from set_class import mySet

set1 = mySet()
set1.add(1)
set1.add(2)

set2 = mySet()
set2.add(1)
set2.add(3)

set3 = set1.copy()
print set1.issubset(set2)
print set1.issuperset(set2)
set1.union(set2)
print set1
print set1.issuperset(set2)
print set3
