#Python error handling 

x  = int(input("Enter value for x \n"))
try:
    if x<0:
        raise Exception("x is negative")
    elif x==0:
        raise Exception("x is zero")

except Exception as e:
    print(e)
    
else:
    print(f'You entered value: {x}')
    print('Program run sucessfully')
    
finally:
    print('Executing regardless wheather program is sucessful or not')