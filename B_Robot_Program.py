for _ in range(int(input())):
    n, x , k = map(int, input().split())
    point = x
    ans = 0
    s=input()
    ff=0
    for i in range(n) :
        if s[i]== "L" : point -=1
        else : point +=1
        k-=1
        if point ==0 : ans +=1 ; ff= 1; break
        if k==0 : break
    f=0
    if ff==1: 
        for i in range(n) :
            if s[i]== "L" : point -=1
            else : point +=1
            k-=1 
            if point ==0 : ans +=1 ;f=1; break
            if k==0 :f=0; break
    if f==1:
        x = i + 1
        ans += (k//x)
    print(ans)
