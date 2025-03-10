for _ in range(int(input())):
    L=list(map(int, input().split()))
    L.sort()
    print(L[2]-L[1]+ L[1]-L[0])