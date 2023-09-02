def viken(num):
    if num==1 or num==0:
        return 1
    return num*viken(num-1)
num = int(input("enter the number --> "))
    
print(viken(num))