# a ={1,2,3,4,5,6,7,8,9}
# print (type(a))
# print (a)

a = set ()
print (type (a))
a.add(5)
a.add(6)
a.add(7)
a.add((1,2,3))
print (len(a)) 
a.remove((1,2,3))
print (a)