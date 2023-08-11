f=open("four.txt","a")
f.write("what is your name")
f1=open("four.txt","r")
f2=f1.read()
for i in f2:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        a=open("four2.txt","a")
        a.write(i)
      
    else:
        a1=open("four3.txt","a")
        a1.write(i)
       
    