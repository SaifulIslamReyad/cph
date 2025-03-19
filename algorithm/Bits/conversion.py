from icecream import ic
def convert_to_bin(x):
    s=""
    while x:
        div = x%2
        s+= str(div)
        x = x//2
    return s[::-1]
ic(convert_to_bin(5))


def convert_to_dec(s):
    s= s[::-1] #n
    n = len(s) 
    ans = 0
    for i in range(n):
        ans += int(s[i])*(2**i) #n
    return ans
ic(convert_to_dec("1000"))

def convert_to_dec_efficient(s):
    return int(s, 2) #O(n) but constant factor is reduced

def convert_to_bin_efficient(n):
    return bin(n)[2:]
ic(convert_to_dec_efficient("1000"))
ic(convert_to_bin_efficient(9))

