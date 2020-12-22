#module contains function defination for finding middle character, count no. of vowels, calculate length and count no. of words in string

#find middle character
def getmiddle(seq):
    l = getlen(seq)
    middle = (0+l-1)//2
    return seq[middle]

#find length
def getlen(seq):
    return len(seq)

#count no. of vowels
def countvowel(seq):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in seq:
        if i in vowels:
            count+=1
        else:
            pass
    return count

#count no. of words
def countword(seq):
    wordlist=seq.split()
    return len(wordlist)
