for _ in range(int(input())):
    ans = temp = c = 1
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10 and b > temp:
            temp = b
            ans = c
        c += 1
    print(ans)
