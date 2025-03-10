def third_root(x):
    if x == 1:
        return 1
    l = 1
    h = x // 2
    while l <= h:
        m = (l + h) // 2
        y = m * m * m
        if y == x:
            return m
        elif y < x:
            l = m + 1
        else:
            h = m - 1
    return l-1


for _ in range(int(input())):
    print(third_root(int(input())))