from icecream import ic
def bin_exp(base, power, mod):
    result = 1
    base %= mod
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        power //= 2
    return result

def sabbir(n):
    mod = 10**9 + 7
    jor = (n + 1) // 2
    bijor = n // 2
    result = (bin_exp(5, jor, mod) * bin_exp(4, bijor, mod)) % mod
    print(result)

sabbir(50)

