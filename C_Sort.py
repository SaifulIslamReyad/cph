for _ in range(int(input())):
    a,n = map(int, input().split())
    s1=input()
    s2=input()
    for i in range(n):
        d={}
        x,y = map(int, input().split())
        x-=1; y-=1
        ans = 0
        for j in range(x,y+1):
            d[s1[j]] = d.get(s1[j], 0) - 1
            d[s2[j]] = d.get(s2[j], 0) + 1
        for value in d.values():
            if value < 0 : ans += abs(value)
        print(ans)