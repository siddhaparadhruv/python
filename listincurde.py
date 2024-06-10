a=[]

while(True):
    print("1.inseet")
    print("2.update")
    print("3.delete")
    print("4.display")
    print("0.exit")
    a1=int(input("enter your choice = "))
    if(a1==1):
        a2=input("enter value for add = ")
        a.append(a2)
        print(a)
    elif(a1==2):
        a3=input("enter  value of element = ")
        a4=input("enter value for update = ")
        z=a.index(a3)
        a[z]=a4
        print(a)

    elif(a1==3):
        a5=input("search value for delete = ")
        a.remove(a5)
    elif(a1==4):
        print(a)
    elif(a1==0):
        print("byyyy")
        break
    else:
        print("invalid")