for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = 0
    mn = 0
    for i in range(n):
        # print("i",i)
        pot = []
        mnOpe = mn + a[i]
        mxOpe = mx + a[i]
        pot.append(mnOpe)
        pot.append(abs(mnOpe))
        pot.append(mxOpe)
        pot.append(abs(mxOpe))
        # print("pot",pot)
        mx = max(pot)
        mn = min(pot)
        # print("mn ,mx", mn,mx)
    print(mx)