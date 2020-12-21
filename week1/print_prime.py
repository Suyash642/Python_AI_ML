#Program will print all prime numbers in the matrix

#for checking ele is prime or not
def isprime(ele):
    if ele <= 1:
        return False
    else:
        for i in range(2,ele):
            if ele % i == 0:
                return False
        return True

#for printing prime numbers
def getprime(matrix):
    for i in matrix:
        for j in i:
            flag = isprime(j)
            if flag is True:
                print(j)
            else:
                continue

#sample matrix
#matrix = [[-1,3,11], [0,9,6], [7,2,3]]    #3x3 matrix

#input from user
row = int(input("Enter no. of rows \n"))
col = int(input('Enter no. of columns \n'))

matrix = [[int(input()) for y in range(col)] for x in range(row)]

for x in matrix:    #printing matrix
    print(x)

if __name__ == "__main__":
    getprime(matrix)