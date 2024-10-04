import math
def combination(n, r):
    if n < r:
        return 0
    if r == 0 or n == r:
        return 1
    r = min(r, n - r)  
    numer = 1
    denom = 1
    for i in range(1, r + 1):
        numer *= n
        denom *= i
        n -= 1
    return numer // denom


# import math
# def combination(n, r):
#     if n < r:
#         return 0 
#     return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))