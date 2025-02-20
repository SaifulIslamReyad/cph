n=int(input())
L=list(map(int, input().split()))
s=sum(L)
print('NO' if s%2==1 or max(L)>(s//2) else 'YES')