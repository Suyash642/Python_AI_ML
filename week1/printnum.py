#Program for printing all numbers till 10 except 3 and 7 using for and while

#using for
print('Using for')
for i in range(1,11):
    if i == 3 or i==7:
        continue
    else:
        print(i)

#using while
print('Using while')
i=1
while i<=10:
    if i == 3 or i==7:
        i+=1
    else:
        print(i)
        i+=1
