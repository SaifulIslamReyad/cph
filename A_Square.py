for _ in range(int(input())):
    L=[]
    for i in range(4):
        L.append(list(map(int, input().split())))
    L.sort()
    print(abs(L[0][1]- L[1][1])**2)