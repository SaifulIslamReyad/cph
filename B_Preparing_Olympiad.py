def powerset(n,SET,l,r,x):
    c=0
    ans=0
    for i in range(2**n):
        
        subset= []
        for j in range(n):
            if (i & (1 << j)):
                subset.append(SET[j])
        if len(subset)<2: continue
        mini = min(subset) 
        maxi = max(subset)
        summ = sum(subset)
        if maxi-mini >= x and summ >= l and summ  <=r : ans+=1 
    return ans

n,l,r,x = map(int, input().split())
L=list(map(int, input().split()))
print(powerset(n,L,l,r,x))