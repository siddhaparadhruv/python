a=int(input("entre the value"))
if(a%5==0 and a%11==0 ):
    print("divisable by 5 and 11")
elif a%5==0:
    print("divisble by 5")	
elif a%11==0:
    print("divisable by 11")	
else:
    print("invalid")