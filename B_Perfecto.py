reyad = [1, 8, 49, 288, 1681, 9800, 57121, 332928]
for _ in range(int(input())):
    n=int(input())
    if n in reyad : print(-1) ; continue
    L= []
    LL= []
    for i in range(1,n+1):
        if i not in reyad:
            L.append(i)
            L.extend(LL)
            LL.clear()
        else: LL.append(i) ; f=1
    print(*L)