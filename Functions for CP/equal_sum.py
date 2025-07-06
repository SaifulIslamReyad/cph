# spliting the array into closer sums


def using_bit(L):
    s = sum(L)
    n = 1 << len(L) - 1
    ans = float("inf")
    for i in range(n + 1):
        c = 0
        for j in range(len(L)):
            if 1 << j & i:
                c += L[j]
        ans = min(ans, abs(s - 2 * c))
    return ans


# n=int(input())
# print(using_bit(list(map(int, input().split()))))
