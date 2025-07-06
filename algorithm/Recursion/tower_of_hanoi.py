def hanoi(n,start,end,c,L):
    if n==1: L.append((start,end)) ; c[0]+=1 ; return
    other = 6- start - end
    hanoi(n-1,start, other,c,L)
    L.append((start,end)) ; c[0]+=1
    hanoi(n-1,other,end,c,L)
c=[0]
L=[]
hanoi(int(input()),1,3,c,L)
print(c[0])
for i,j in L: print(i,j)