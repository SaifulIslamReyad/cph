for _ in range(int(input())):
    n=int(input())
    L=list(map(int, input().split()))
    x = ((sum(L)+1)*(-1)//2)
    y = L.count(-1) % 2 
    print(max(x,y))
