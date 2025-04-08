for _ in range(int(input())):
    L= []
    n,m = map(int, input().split())
    for i in range(n):
        L.append(input())
    c=0
    for i in range(n):
        c+= L[i].count('1') % 2
    cc=0
    for i in range(m):
        ccc=0
        for j in range(n):
            ccc += int(L[j][i]) 
        cc+=ccc%2
    print(max(cc,c) + abs(cc-c)%2)