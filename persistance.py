def persistence(n):
    sum,x = n,n
    count=0
    while sum>=10:
        x=sum
        sum=1
        count+=1
        
        while x>0:
            ##print(x%10)
            sum =sum * (x%10)
            x//=10
        ##print(sum)    
    
    return count

        