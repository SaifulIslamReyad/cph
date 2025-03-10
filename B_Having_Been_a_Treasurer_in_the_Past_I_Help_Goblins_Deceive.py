for _ in range(int(input())):
    n=int(input())
    s=input()
    up = under = 0
    for i in range(n):
        if s[i]=='-': up+=1
        else: under+=1
    x= int(up //2)
    x= x* (up -x )
    print(x*under)