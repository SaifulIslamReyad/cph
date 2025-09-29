# from icecream import ic as print
import math 

for _ in range(int(input())):
    n=int(input())
    L=list(map(int, input().split()))
    x= 1
    for i in range(n):
        x*=L[i]
    y= int(math.sqrt(x))
    if y**2 != x and x!=1 : print(-1) ; continue
    nn=1
    f=0
    m=-1
    for i in range(n):
        nn*=L[i]
        if nn==y: f=1 ; m=i+1 ;break
    if f==0 : print(-1)
    else : print(m)