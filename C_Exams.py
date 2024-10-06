L=[]
for _ in range(int(input())):
    LL= list(map(int, input().split()))
    L.append(LL)
L.sort()
x=min(L[0])
for LL in L[1:]:
    if LL[1]<x: x= LL[0]
    else : x= LL[1]
print(x)