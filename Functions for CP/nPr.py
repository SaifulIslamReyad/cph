import math
def permutation(n, r):
    if n < r:
        return 0  
    return math.factorial(n) // math.factorial(n - r)