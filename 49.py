from itertools import product


def viken(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

s = viken(7)
print(s)