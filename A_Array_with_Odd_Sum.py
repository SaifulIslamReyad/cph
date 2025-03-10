for _ in range(int(input())):
    n=int(input())
    L=list(map(int, input().split()))
    if sum(L)%2==1: print("YES") ; continue
    even = odd = 0
    for i in range(n):
        if L[i]%2==0: even+=1
        else : odd +=1
    if even==0 or odd== 0 : print("NO")
    else: print("YES")