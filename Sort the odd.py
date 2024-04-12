'''
Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
'''
##
##'''
def sort_array(source_array):
    ac=source_array.copy()
    for i in range (len(source_array)):
        #print(i)
        if(source_array[i]%2==1):
            for j in range(i+1,len(source_array)):
               # print(j)
                if(source_array[j]%2==1):
                    if(source_array[i]>source_array[j]):
                        temp=source_array[i]
                        source_array[i]=source_array[j]
                        source_array[j]=temp
    print(source_array)
sort_array([5, 3, 2, 8, 1, 4])
##'''
##
'''
def sort_array(source_array):
    a=[]
    for i in source_array:
        if(i % 2!=0):
            a.append(i)
    #print(source_array)       
    a.sort()
    #print(a) 
    for j in source_array:
        if j%2!=0:
            source_array.= a[j]

    print(source_array)        
sort_array([5, 3, 2, 8, 1, 4])
'''