from itertools import permutations
import bisect


def unique_digit_combinations(len):
    ordhekLen = len//2
    s = ordhekLen*"4" + ordhekLen*"7"
    perm = set(permutations(s))
    return [int(''.join(p)) for p in perm]


s=input()
len = len(s)
n = int(s)
if len%2==1: print(((len+1)//2)*"4"+((len+1)//2)*"7")
else: 
    LL = sorted(unique_digit_combinations(len))
    LL.append(int(((len//2)+1)*"4" + ((len//2)+1)*"7"))
    if LL[bisect.bisect_right(LL,n)-1]==n: print(n)
    else:print(LL[bisect.bisect_right(LL,n)])

