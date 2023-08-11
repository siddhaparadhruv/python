import pickle

f=open("four.txt","ab")
pickle.dump("what is your name",f)
f1=open("four.txt","rb")
f2=pickle.load(f1)
for i in f2:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        a=open("four2.txt","ab")
        pickle.dump(i,a)
      
    else:
        a1=open("four3.txt","ab")
        pickle.dump(i,a1)
       
    