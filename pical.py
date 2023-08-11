import pickle
f=open("four.txt","ab")
pickle.dump("what is your name",f)
f1=open("four.txt","rb")
f2=pickle.load(f1)

