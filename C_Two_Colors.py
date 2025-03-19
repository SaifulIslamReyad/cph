from bisect import bisect_left
# from icecream import ic

for _ in range(int(input())):
    n,m=map(int, input().split())
    L=sorted(list(map(int, input().split())))
    ans=0
    for i in range(1,n//2+1):
        x=m-bisect_left(L,i)
        y=m-bisect_left(L,n-i)
        ans+= (x-1)*y 
        # ic(i,x,n-i, y,ans)
    ans*=2
    if n%2==0: ans-= (x-1)*y


    print(ans)