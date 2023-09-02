
def viken(num1,num2,num3):
    if  (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3

# mun1  = int(input("enter the number --> "))
# mun2  = int(input("enter the number --> "))
# mun3  = int(input("enter the number --> "))

print(viken(45,46,47))