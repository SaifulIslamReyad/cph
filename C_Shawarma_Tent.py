# https://codeforces.com/contest/1271/problem/C
n,x,y=map(int,input().split())
a,b,c,d=0,0,0,0
for i in range(n):
	p,q=map(int,input().split())
	if(p>x):
		a+=1
	if(p<x):
		b+=1
	if(q>y):
		c+=1
	if(q<y):
		d+=1
		
ans=max(a,b,c,d)    
print(ans)
if d==ans:
	print(x,y-1)
elif a==ans:
	print(x+1,y)
elif c==ans:
	print(x,y+1)
elif b==ans:
	print(x-1,y)