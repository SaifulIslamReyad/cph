# T(n) = f(n) + a * T(n-b)
# O(a^(n/b)*O(f(n))
# a = kotobar call deya hoiche 
# O(n*O(f(n)))



# here , a= 2, b= 1, O(f(n))= O(1)
# O(2^(n)*O(1) = O(2^n)



# 1 + 2 + 4 + 8
# 2^0 + 2^1 + 2^2 + 2^3.....+ 2^n
# a= 1
# n= n
# r= 2
# 2(2^n  - 1)= 2^n


from time import time
from functools import lru_cache


def sajib(n,a=0):
    if n<=0 : return
    # print(n,  end = " ")
    a+=1
    sajib(n-1)  
    sajib(n-1)

@lru_cache(maxsize=None)
def fibo(n):
    if n<2: return n
    return fibo(n-1) + fibo(n-2)

start = time()    
fibo(32)
end = time()
print(end-start)
print(fibo.cache_info())