a={}
while(True):
    print("1.inseet")
    print("2.update")
    print("3.delete")
    print("4.display")
    print("0.exit")
    a1=int(input("enter your choice = "))
    if(a1==1):
        a2=input("enter key for add = ")
        a6=input("enter value for add = ")
        if(a2==a.keys):
            print("enter valid key")
        else:    
            a[a2]=a6
            print(a)
    elif(a1==2):
        a3=input("search value for update = ")  
        a4=input("enter value for update = ")
        
        a[a3]=a4
        print(a)

    elif(a1==3):
        a5=input("search value for delete = ")
        a.clear(a5)
    elif(a1==4):
        print(a)
    elif(a1==0):
        print("byyyy")
        break
    else:
        print("invalid")
