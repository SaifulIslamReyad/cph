import math
for _ in range(int(input())):
    n,h = map(int, input().split())
    L=list(map(int, input().split()))
    LL= [0]*n
    for i in range(n-1):
        LL[i]= L[i+1]-L[i]
    LL[n-1]= 1000000000
    LL.sort()
    x= h/n
    for i in range(n):
        c=0
        if i==n-1:
            break
        if LL[i]<=x:
            h -= LL[i]
            x= h/(n-i-1)
        else: break
    x = math.ceil(x)
    print(x)
    
    
    
    