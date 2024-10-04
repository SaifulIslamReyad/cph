m,s=map(int,input().split())
if s<1:print(-(m>1),-(m>1)),exit()
if 9*m<s:print(-1,-1),exit()

a=''
for i in range(m):
    temp=min(9,s)
    a+=str(temp)
    s-=temp
c=a[::-1]
if a[-1]>'0' :
    b=a[::-1]
else:
    b="1"
    for i in range (1,m):
        if c[i]>'0':
            # print(i)
            # print(c[i])
            x= c[0:i:1]
            y= int(c[i])
            y-=1
            x+=str(y)
            # print(x)
            if i<m-1:
                x+=c[i+1::1]
            break
    b+=x[1::1]
    

print(b,a)
