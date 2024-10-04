x=2
l=[1]
j=0
while(l[j]<=800):
    l.append(l[j]+x)
    x+=1
    j+=1
# 1,3,6,10,15
s=[1]
x=0
j=1
while s[x]<=10001:
    s.append(s[x]+l[j])
    x+=1
    j+=1
# 1,4,10,20,35
