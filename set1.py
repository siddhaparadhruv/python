s={1,2,3,4,5,6,"hi",7,8}
s1={1,2,"hello"}
#print(type(s))
print(dir(s))
s.add("hello")

#print(s.intersection(s1))
#print(s.difference_update(s1))
print(s.difference(s1))
print(s)
#print(s1)
print(s1.issuperset(s))
print(s1.issubset(s))
print(s1.pop())
print(s1)
#print(s.remove())
print(s)
print(s.union(s1))
#help(s.difference_update)