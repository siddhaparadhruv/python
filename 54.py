def viken(n):
    for i in range(n):
        print("*" * (n-i) )
n = int(input("enter the number --> "))
v = viken(n)
print(v)