n=int(input())
L=[]
powerset=[]
for i in range(n):
    L.append(int(input()))
s = 2**n
f=0
for i in range(s):
    ans= 0
    for j in range(n):
        if (1<<j) & i : ans += L[j]
        else : ans -= L[j]
    if ans % 360 == 0 : print("YES") ;f=1; break
if f==0: print("NO")    