alist = [{'username': 'a', 'password': 'a'}]
blist = [{'que': 'q', 'op': ['w', 'e', 'r', 't', 't']}]
clist = [{'username':'a' , 'password':'a'}]
while(True):
    print("|---------|")
    print("|1.admin  |")
    print("|2.student|")
    print("|0.procees|")
    print("|---------|")
    print("===========================")
    a=int(input("enter your choice = "))
    if(a==1):
        while(True):
            print("|---------|")
            print("|1.rigster|")
            print("|2.login  |")
            print("|0.exit   |")
            print("|---------|")
            print("===========================")
            c=int(input("enter your choice = "))
            if(c==1):
                d={}
                print("===========================")
                f=(input("enter your name = "))
                print("===========================")
                g=(input("enter your email = "))
                d['username']=f
                d['password']=g  
                print("-----------------------------------------")
                print(d)
                alist.append(d)
            elif(c==2): 
                flag=0
                print("========================")
                z=(input("enter your name = "))
                print("========================")
                e=(input("enter your email = "))
                for i in alist:
                    if(i['username']==z and i['password']==e):
                        flag=1
                        print("found") 
                        while(True):
                            print("|--------------------------|")
                            print("|1. add Qestion            |")
                            print("|2. remove Qestion         |")
                            print("|3. update Qestion         |")
                            print("|4. dips Qestion           |")
                            print("|5. give answer of Qestion |")
                            print("|0.Exit                    |")
                            print("|--------------------------|")
                            print("============================")
                            ch=int(input("Enter your chocie = "))
                            dl={}
                            if ch==1:
                                print("============================")
                                fq=(input("enter your question = "))
                                print("=========================")
                                op1=(input("enter your MCQ 1 = "))
                                op2=(input("enter your MCQ 2 = "))
                                op3=(input("enter your MCQ 3 = "))
                                op4=(input("enter your MCQ 4 = "))
                                print("=========================")
                                op5=(input("enter right MCQ  = "))
                                if op5==op1 or op5==op2 or op5==op3 or op5==op4:
                                    print("*** right answer ***")
                                    dl['que']=fq                        
                                    dl["op"]=[op1,op2,op3,op4,op5]                        
                                    blist.append(dl)
                                else:
                                    print("--- not posibal ---")                                
                            elif ch==2:
                                flegde=0
                                c1=-1;
                                print("====================================")
                                fd=(input("enter your question for delete= "))
                                for i in blist:
                                    c1=c1+1
                                    if i['que']==fd:
                                        flegde=1
                                        print("*** deleted ***")
                                        blist.pop(c1)
                                if flegde!=1:
                                    print("--- not delete ---")
                                #dl['delete']=fd
                                print("====================================")
                                print(blist)
                            elif ch==3:
                                fleg1=0
                                print('update')
                                print("=======================================")
                                a2=(input("search your  question for update = "))
                                for i in blist:
                                    if i['que']==a2:
                                        fleg1=1
                                        print("*** search ***")
                                        print("==========================")
                                        i['que']=(input("enter your question = "))
                                        op1=(input("enter your MCQ 1 = "))
                                        op2=(input("enter your MCQ 2 = "))
                                        op3=(input("enter your MCQ 3 = "))
                                        op4=(input("enter your MCQ 4 = "))
                                        op5=(input("enter your MCQ 5 = "))
                                        print("=========================")
                                        
                                        if op5==op1 or op5==op2 or op5==op3 or op5==op4:
                                            print("right answer")
                                            print("hi")
                                            i["op"]=[op1,op2,op3,op4,op5]                                             
                                        else:
                                            print("not posibal")                                
                                if fleg1!=1:
                                    print("not search")

                            elif ch==4:
                                print(blist)
                            elif ch==5:
                                fla=0
                                print(fq)
                                print(op1)
                                print(op2)
                                print(op3)
                                print(op4)
                                ans=(input("enter the right answer = "))
                                for i in clist:
                                    if(op5==ans):
                                        fla=1
                                        print("your MCQ is right") 
                                if fla != 1:
                                    print("your MCQ is wrong")    
                            elif ch==0:
                                break
                            else:
                                print("invalid")
                if flag != 1:
                    print("not found")
            elif(c==0):
                break
            else:
                print("invalid")
                    
    elif(a==2):
        while(True):
            print("|==================|")
            print("|welcome to student|")
            print("|==================|")
            print("***********************")
            print("|---------------------|")
            print("|1.rigster for student|")
            print("|2.login for student  |")
            print("|0.exit               |") 
            print("|---------------------|")
            print("===========================")
            Q=int(input("enter your choice = "))
            if(Q==1):
                    if(Q==1):
                        ds={}
                        print("===========================")
                        f=(input("enter your name = "))
                        print("===========================")
                        g=(input("enter your email = "))
                        ds['username']=f
                        ds['password']=g  
                        print("-----------------------------------------")
                        print(ds)
                        clist.append(ds)
            elif(Q==2): 
                flag=0
                print("========================")
                z=(input("enter your name = "))
                print("========================")
                e=(input("enter your email = "))
                c3=0;
                for i in clist:
                    if(i['username']==z and i['password']==e):
                        flag=1  
                        print("*** found ***") 
                        for i in blist:
                            print(i['que'])
                            for j in range(len(i['op'])-1):
                                print(i['op'][j])
                            answer=(input("enter the right answer = "))
                            if i["op"][4]==answer:
                                c3=c3+1
                if flag != 1:
                    print("--- not found ---")
                print(c3,"/",len(blist))                            
            elif(Q==0):
                break
            else:
                print("invalid")
    elif(a==0):
        print("|*****************************|")
        print("|!!! THANK FOR WISITING AS !!!|")
        print("|*****************************|")
        break;
    else: 
        print("invalid")