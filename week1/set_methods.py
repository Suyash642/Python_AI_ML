#This program contains diff set methods

#declaring sets
set1 = set()
set2 = set()

#add method
for i in range(1,6):
    set1.add(i)
for i in range(4,10):
    set2.add(i)
print(set1)
print(set2)

#union method
union_set = set1.union(set2)
print(union_set)

#intersection method
intersect_set = set1.intersection(set2)
print(intersect_set)

#difference method
difference_set = set1.difference(set2)
print(difference_set)

#isdisjoint() method
print(set1.isdisjoint(set2))
print(intersect_set.isdisjoint(difference_set))

#clear method
sampleset=set([4,2,5,6])
print(sampleset)
sampleset.clear()
print(sampleset)

#enumerate method
print(set(enumerate(set1)))
for count, item in enumerate(set1):
    print(count, item)

#sum method
print(sum(union_set))