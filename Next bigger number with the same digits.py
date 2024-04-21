'''
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1

'''
##
def next_bigger(n):
    n=str(n)
    a=list(n)
    #print(a)
    c=0
    i=len(a)-1
    while(i>0):
        if(a[i]>a[i-1]):
            temp=a[i]
            a[i]=a[i-1]
            a[i-1]=temp
            c+=1
            i-=1
        if(c==1):
            break
        else:
            i-=1
            continue
    if c==0:
        return (-1)
    
    

    x = int(''.join(map(str, a)))
    print(x)


next_bigger(1234567890)