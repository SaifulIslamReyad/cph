from functools import lru_cache
from time import time 
from icecream import ic

# maxsize is cache size, default 128
# currsize : how many values are cached currently
@lru_cache(maxsize=128, typed=False) #try to run after commenting this
def count_vowels(s)-> int :
    return sum(s.count(vowel) for vowel in "AEIOUaeiou")


def test()->None:
    sentences : list[str] = [ "hello world", "no way home ", "oi kire"]
    for s in sentences:
        for i in range(1000000): count_vowels(s)
# 3 million func calls will be just 3 func calls

if __name__ == "__main__":
    start= time()
    test()
    end= time()
    ic(end-start)
    ic(count_vowels.cache_info())
    count_vowels.cache_clear()
    ic(count_vowels.cache_info())


# if type= True : then func(10) and func(10.0) will be stored separately
# lru cache uses dictionary to store cache results
# so func(a=5,b=3) and func(b=3,a=5) will be considered different
