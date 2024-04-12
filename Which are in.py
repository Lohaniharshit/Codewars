'''
Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: In some languages r must be without duplicates.

'''
## https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

def in_array(array1, array2):
    a1=array1.copy()
    a2=array2.copy()
    c=[]
    if a1 in a2:
        c.append(a1)

    print(a1)


in_array(["live", "arp", "strong"],["lively", "alive", "harp", "sharp", "armstrong"])