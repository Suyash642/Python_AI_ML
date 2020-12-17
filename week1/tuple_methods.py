#This program contains the different methods of tuples

#declaring and displaying tuple
sample = (1,"hello",12.5,100,1,2.5)
print(sample)

#count method
print(sample.count(1))

#index method
print(sample.index('hello'))
print(sample.index(1)) #gives first occurence of element

#del method
newsample = (1,2,3)
print(newsample)
del(newsample)
#print(newsample)

#slicing in tuple
print(sample[2:4])
print(sample[:-4])
print(sample[:])

#len method
print(len(sample))

