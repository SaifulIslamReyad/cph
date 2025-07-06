import math as m
for _ in range(int(input())):
    n,k=map(int, input().split())
    if n<=k: 
        print(int(m.ceil(k/n)))
    else :
        if n%k==0 : print(1)
        else: print(2)
