import pickle
#coad for add first value
'''
f=open("one.txt","ab")
pickle.dump("what is your name",f)
'''
a1=open("two.txt","rb")
a2=pickle.load(a1)
c=open("three.txt","ab")
pickle.dump(a2,c)
'''
f1=open("one.txt","rb")
f2=pickle.load(f1)
#coad for add secound value
a=open("two.txt","ab")
pickle.dump("my name is dhruv",a)
pickle.dump(a2,c)
c=open("three.txt","ab")
pickle.dump(a2,c)
pickle.dump(f2,c)
print(c)
'''