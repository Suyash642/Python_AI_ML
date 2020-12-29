try:
    with open('C:\Codewayy Tasks\week1\demo.txt','r') as f:
        print(f.read())

except FileNotFoundError:
    print('file doesnot exist')
    
else:
    f.close()