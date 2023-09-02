def asc(arr):
    a=[]
    for i in range(0,10):
        if a[i]==len(numbers):
            print(len(numbers))
        

def dsc(arr):
    a=[]
    for i in range(0,len(arr)):
        if a[i]==len(numbers):
            print(len(numbers))


numbers = [5, 2, 9, 1, 5, 6]

print("Original Numbers:", numbers)

asc(numbers)
print("Ascending Sorted:", numbers)

dsc(numbers)
print("Descending Sorted:", numbers)
