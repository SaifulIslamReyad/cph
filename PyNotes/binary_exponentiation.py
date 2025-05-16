from icecream import ic
import math
def power(a,n):
    if n==0: return 1
    if int(n)==1: return a
    temp = power(a, n/2)
    return temp * temp


ic(math.pow(2,4))
ic(power(2,4))