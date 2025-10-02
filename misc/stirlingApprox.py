from math import *

def ferr(n):

    X = log(factorial(n))
    S = (n * log(n)) - n
    dX = S - X

    return [X, S, dX/X]

n = 1000

for i in range(3):
    print(ferr(n)[i])