#module for getting square of no., maximum and minimum no. of list and sum of list

#square of number
def getsquare(ele):
    return ele**2

#maximum number of list
def getmax(lis):
    max_num = lis[0]
    for i in range(1,len(lis)):
        if max_num < lis[i]:
            max_num = lis[i]
        else:
            continue
    return max_num

#minimum number of list
def getmin(lis):
    min_num = lis[0]
    for i in range(1,len(lis)):
        if min_num > lis[i]:
            min_num = lis[i]
        else:
            continue
    return min_num

#sample lis
#lis = [12,85,21,14,17,100,30,10,-1, -3]

#sum of all numbers in list
def getsum(lis):
    s = 0
    for i in lis:
        s+=i
    return s