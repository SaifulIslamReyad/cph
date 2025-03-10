# from icecream import ic
# ic.disable()
def peak1 ( L):
    n = len(L)
    if n==1  or L[0] > L[1] : return 0 ; 
    if L[n-1] > L[n-2] : return n-1
    l= 0
    h= n-1
    m = (h+l)//2
    while l<=h:
        m = (h+l)//2
        # ic(L,l,h,m) 
        if m>0 and L[m]>L[m-1] and L[m] > L[m+1]:
            return m
        elif (m>0 and L[m]>L[m-1]) or (m<n-1 and L[m] < L[m+1]): 
            l = m+1
        else : 
            h = m-1
    return -1
for _ in range(int(input())):
    L=list(map(int, input().split()))
    print(peak1(L))
    


