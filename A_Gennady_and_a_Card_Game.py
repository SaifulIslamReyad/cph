s=input()
L=list(input().split())
f=0
for i in L:
    if i[0]==s[0] or i[1]==s[1]:
        f=1
        break

if f: print('YES') 
else: print("NO")