t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    L = list(map(int, input().split()))
    l = 1
    r = h
    while l <= r:
        m = (l + r) // 2
        s = m
        for i in range(1, n):
            s += min(m, L[i] - L[i-1])
        if s < h:
            l = m + 1
        else:
            r = m - 1
    print(r + 1)