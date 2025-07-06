for _ in range(int(input())):
    a,b= map(int, input().split())
    x=input()
    s=input()
    c=f=0
    for i in range(6):
        if s in x :f=1; break
        x+=x
        c+=1
    if f: print(c)
    else: print(-1) 