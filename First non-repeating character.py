'''

Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.

'''
##code
'''
def first_non_repeating_letter(s):
    c=0
    s.lower()
    
    a=[]
    if(len(s)<1):
        print('')
    else:

        #print(dir(a))
        for ch in s:
         a.append(ch)

        for i in range(0,len(a)):
            for j in range(i+1,len(a)):
                 if(a[i]!=a[j]):
                     c+=1
                #if(c==1):
                      #  break
                
        
    print(a[i])

first_non_repeating_letter('stress')
'''
##
'''
def first_non_repeating_letter(s):
    c=0
    a=list(s)
    d=[]
    #print(dir(s))
    for i in range(len(a)):
        
        for j in range(len(a)):
            if(a[i]!= a[j]):
                continue
            if(a[i] not in d):
                d.append(a[i])
                
    #print(d)
    for i in d:
        c=a.count(i)
        #print(c)
        if(c==1):
            print(i)
            break
                
              
    #print(a[i])

first_non_repeating_letter('stress')
'''
##
def first_non_repeating_letter(s):
    str = s.lower()
    for i in s:
        if str.count(i.lower())==1 : 
           return i
    return ''