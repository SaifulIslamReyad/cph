s=input()
n= len(s)
f=0
for i in range(n-1,-1,-1):
    if s[i]=='1': continue
    elif i>0 and s[i]=='4' and s[i-1]=='1' : i-=1 ; continue
    elif i>1 and s[i]=='4' and s[i-1]=='4' and s[i-2]=='1' : i-=2 ; continue
    else: f=1 ; break
print("YNEOS"[f::2])