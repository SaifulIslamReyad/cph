from functools import lru_cache
from time import time 
from icecream import ic

#easily exceed default maxsize 128
@lru_cache(maxsize=None) 


def fibonacci(n)->int:
    if n<2: return n
    return fibonacci(n-2) + fibonacci(n-1)

def test()->None:
    ans : int = fibonacci(300)
    ic(ans)


if __name__== "__main__":
    st= time()
    test()
    ic(time()- st)
