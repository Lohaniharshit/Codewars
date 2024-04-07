def order(s):
  
  l = len(s)
  ##print (l)
  arr=[]
  sl= list(s)
  for i in range(l):
     ch = sl[i]
        ##print(ch)
     if ch.isdigit():
          arr.append(int(ch))
     else:
        continue
      
     ##print(arr)
  ##arr1= [int(char) for char in arr]
  arr=sorted(arr)
  ##print(arr)
  index=0
  for i in range(l):
        ch1 = sl[i]
        ##print(ch)
        if ch1.isdigit():
          ##print(ch)
          sl[i]=str(arr[index])
          index+=1
        else:
            continue
  result=''.join(sl)     
  print(result)



order("is1 Thi2s T3est 4a")