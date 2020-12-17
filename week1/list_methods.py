#This program contains different methods on list

#declaring and displaying list
list = [1,2,3,4,5,6]
print(list)

#append method
list.append(7)
list.append('python')
print(list)

#remove method
list.remove('python')
print(list)

#sum method
print(sum(list))

#extend method
list.extend([11,12,13,14,15,16])
print(list)

#count method
print(list.count(5))

#insert method
list.insert(5,5)
print(list)

#max and min method
print(max(list))
print(min(list))

#len method
print(len(list))