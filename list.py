a = [1,2,3,5,2,3,3,2,1]
print(a[1])
#print(a[9])
#print(a[9])
#print(a[-9])
#print(dir(a))
a.append(5)
print(a)
print(a.count(100))
print(a.index(3))
a.insert(2,100)
print(a)
a.pop(3)
print(a)
a.remove(5)
print(a)
a.reverse()
print(a)
a.sort(reverse=True)
print(a)
#help(a.sort)