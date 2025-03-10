from icecream import ic
# ic.disable()
def maximumUnits(L, n):
    ans= 0
    L.sort(key = lambda x : x[1], reverse= True)
    ic(L)
    ans =0
    for i in L:
        x = min(n,i[0])
        n-=x 
        ans += x*i[1]
        ic(n,x,ans,i)
        if n==0 : break
        
    return ans
L= [[1,3],[2,2],[3,1]]
n= 4
print(maximumUnits(L,n))