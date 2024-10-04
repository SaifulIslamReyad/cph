def maxSumNonAdjacent(d):
    a=b=0
    for i in d:
        a,b=max(a,i+b),a
    return a
print(maxSumNonAdjacent([4,1,1,2,1,1,2,4,1,2,2,2,3]))