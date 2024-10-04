n, m, k=map(int, input().split())
L=[]
for _ in range(m+1):
    L.append(int(input()))
    
c=0    
for i in range(m):
    if bin((L[i]|L[m])-(L[i]&L[m])).count("1")<=k:
        c+=1
print(c)


# print(bin(5|3)[2:])
