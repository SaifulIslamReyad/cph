for _ in range(int(input())):
    n=int(input())
    LL=list(map(int, input().split()))
    L=set(LL)
    f=1
    if len(L) >= 3 : print("No") ; f=0
    elif len(L)==2: 
        x= LL.count(LL[0])
        y= n-x
        if abs(x-y)>1: print("No"); f=0 ; continue
    if f==1: print("Yes")

