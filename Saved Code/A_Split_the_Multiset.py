# import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    print((n-1+(k-1)-1)//(k-1))
    # print(math.ceil((n-1)/(k-1)))


