import math
for _ in range(int(input())):
    n,k,p  = map(int, input().split())
    ans = math.ceil(abs(k)/p)
    print(ans if ans <= n else -1)  