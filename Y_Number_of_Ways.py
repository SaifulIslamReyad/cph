def x(n,c):
    if n==0:c[0]+=1 ; return
    if n<=2: c[0]+=n; return 
    if n==3: c[0]+=4; return 
    x(n-1,c)
    x(n-2,c)
    x(n-3,c)


a,b = map(int, input().split())
c=[0]
x(b-a,c)
print(c[0])