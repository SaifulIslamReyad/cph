n=int(input())
L=list(map(int, input().split())) +[0]
L.sort(reverse=True)
sum = 0
i=0
for i in range(len(L)):
    if sum >= n : break
    sum+= L[i]
print(i if sum>=n else -1)