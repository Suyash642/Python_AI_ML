#module contains use of logical operators of python

#AND 
def AND(num1, num2, num3):
    if num1>num2 and num2<num3 and num3>num1:
        return True
    else:
        return False

#OR
def OR(num1, num2, num3):
    if num1>num2 or num2<num3 or num3>num1:
        return True
    else:
        return False

#NOT
def NOT(num1,num2):
    if not(num1%2 == 0 or num2%2==0):
        print('num1 or num2 is not divisible by 2')
    else:
        print('num1 or num2 is divisible by 2')