for _ in range(int(input())):
    n,k = map(int, input().split())
    L=list(map(int, input().split()))
    c=0
    cc=0
    for i in range(n):
        if L[i]>=k: c+=L[i]
        if L[i]==0 and c>0: c-=1 ; cc+=1
    print(cc)