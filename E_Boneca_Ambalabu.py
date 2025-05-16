for _ in range(int(input())):
    n=int(input())
    L=list(map(int, input().split()))
    m= 8
    ans=0
    for i in range(n):
        ans+= (m^L[i])
    print(ans)

