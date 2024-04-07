def binary_array_to_number(arr):
  
  rev=arr[::-1]
  dec=0
  l=len(rev)
  for i in range(l):
    ch=rev[i]
    if(ch==1):
      dec=dec+(2**i)

  print(dec)    
binary_array_to_number([0,0,0,1])