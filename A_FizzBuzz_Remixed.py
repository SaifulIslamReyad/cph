for _ in range(int(input())):
    n = int(input())
    ans = (n // 15) * 3
    modu = n % 15

    if modu >= 0: ans += 1
    if modu >= 1: ans += 1
    if modu >= 2: ans += 1

    print(ans)
