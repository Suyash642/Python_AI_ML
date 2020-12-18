#This program contains methods of dictionary

#creating and displaying dictionary 
car = {1:'Mercedes', 2:'BMW', 3:'Ferrari', 4:'Toyota', 5:'Tata'}
print(car)

#copy method
copiedcar = car.copy()
print(copiedcar)

#keys method
keylist = list(car.keys())
print(keylist)

#values method
namelist = list(car.values())
print(namelist)

#update method
car.update({6:'Maruti'})
print(car)

#items method
print(list(car.items()))

#pop method
car.pop(4)  #Remove element/value with specified key
print(car)

#clear method
copiedcar.clear()
print('deleted copiedcar')

#get method
getcar = car.get(2)
print(getcar)
