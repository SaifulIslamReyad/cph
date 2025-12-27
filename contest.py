import math
import bisect
L=[0,1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961]
for _ in range(int(input())):
    n=int(input())
    middle = bisect.bisect_right(L,n//2)
    elements = middle *2 -1 
    middle2 = middle*2 -1
    c = math.perm(elements,2) + middle2
    index = bisect.bisect_right(L,n)
    
    for i in range(middle,index):
        y = bisect.bisect_right(L,n-L[i])
        y = y*2 -1
        y*=4
        c+=y
    print(max(1,c))


