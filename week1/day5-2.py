import math
#math functions
num = 45.47

print(f'Given number is : {num}')
print(f'Celing value is : {math.ceil(num)}')
print(f'floor value is : {math.floor(num)}')

diameter = 20.60
print(f'Circumference of a circle is: {math.floor(math.pi*diameter)}')

angleindegree = 30
angleinradians = math.radians(angleindegree)
print(f'Angle in radians is: {(angleinradians)}')
print(f'sin of angle is: {math.sin(angleinradians)}')

#sorting list, tuples, set
li=[1,6,8,4,3,9,7]
print(f'original list is: {li}')
li.sort()
print(f'Sorted original list is: {li}\n')

tup = tuple(li)
print(f'original tuple is; {tup}')
print(f'sorted new tuple is: {tuple(sorted(tup, reverse = True))}')

s = set([7,8,71,20,36,56])
print(f'original set is: {s}')
print(f'sorted new set is: {sorted(s)}')
