n,k=map(int, input().split())
L1=list(map(int, input().split()))
L2=list(map(int, input().split()))
L3 = list(map(lambda x, y: y // x, L1, L2))
while(k):
    m=min(L3)
    ind= L3.index(m) 
    x=L1[ind]-(L2[ind]%L1[ind])
    if x<=k: k-=x; L3[ind]+=1;L2[ind]+=x 
    else: break
print(min(L3))
