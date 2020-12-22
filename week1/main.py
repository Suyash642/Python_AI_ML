#importing modules
import mod1_list as mod1
import mod2_string as mod2 
import mod3_logical as mod3 

#first module function
samplelist = [1,-1,23,56,2,7,0]

print(f'Square of 8 is: {mod1.getsquare(8)}')

print(f'Max number of list : {mod1.getmax(samplelist)}')
print(f'Min number of list : {mod1.getmin(samplelist)}')

print(f'Sum of list : {mod1.getsum(samplelist)}')

#second module function
string = 'Python'

print(f'Middle character of string is : {mod2.getmiddle(string)}')

print(f'length of string is: {mod2.getlen(string)}')

print(f'Count of vowels: {mod2.countvowel(string)}')

print(f'Count of words : {mod2.countword(string)}')

#Third module function
num1 = 2 
num2 = 1
num3 = 3

print(f'and: {mod3.AND(num1,num2,num3)}')

print(f'or: {mod3.OR(num1,num2,num3)}')

print(f'not: {mod3.NOT(num1,num2)}')