for _ in range(int(input())):
    n=int(input())
    L=list(map(int, input().split()))
    LL=[L[0]]
    for i in range(1,n):
        if L[i]<L[i-1]:
            LL.append(1)
        LL.append(L[i])
    print(len(LL))
    print(*LL)
    