#print(type("hello world"))
#print(type)

'''
import turtle
wn=turtle.Screen()
alex=turtle.Turtle()
alex.forward(150)
alex.left(90)
alex.forward(75)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)
wn.exitonclick()
'''
#
'''
import random
prob= random.random()
print(prob)
dicethrow=random.randrange(1,5)
print(dicethrow)
'''
#
'''
alist=['a','b','c','d','e']
print(alist)
#alist[1:3]= []
#print(alist)
del alist[0]
print(id(alist))
'''
#
'''
a=[81,82,83]
b=a[:]
print(a)
print(b)
#print(a is b)
#b=a
print(a is b)
print(a == b)
b[0]=5
print(a)
print( b)
print(id(a))
print(id(b))
'''
#
'''
scores= [("Rod",-1),("Marlo",1),("You",2)]
for person in scores:
    name=person[0]
    score = person[1]
    print("Hello {}, your score is {}.".format(name,score)) 
    '''
#
