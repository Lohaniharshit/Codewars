'''
Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

Examples (input --> output):
"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"

'''
##
def camel_case(s):
    s=' '+s
    l=[]
    a=list(s)
    for i in range (len(a)-1):
        #print(a[i])
        if(a[i]==' '):
            a[i+1] = a[i+1].upper()
            #print(a[i])
    for i in range (len(a)):
        if(a[i]!=' '):
            l.append(a[i])
        else:
            continue
    st=''.join(l)
    print(st)

camel_case("test case") 