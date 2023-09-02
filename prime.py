num = int(input("enter the nuber --> "))
prime = True

for i in range(2,num):
    if (num%i==0):
        prime = False
    break
if prime:
    print ("the num is prime ")
else:
     print ("the num not is prime ")