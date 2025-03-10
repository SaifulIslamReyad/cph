# from icecream import ic
for _ in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)

    a = -1
    for i in range(n - 1):
        if L[i] == L[i + 1]:
            a = L[i]
            ind = i
            break

    if a == -1:
        print(-1)
        continue
    # ic(L, ind)
    f = 0
    LL = [ind, ind + 1, ind - 1]
    for i in range(len(L) - 1):
        if i not in LL and min(L[i], L[i + 1]) + 2 * a > max(L[i], L[i + 1]):
            f = 1
            print(a, a, L[i], L[i + 1])
            break
    if f == 0 and ind < (n - 2) and min(L[ind-1], L[ind + 2]) + 2 * a > max(L[ind -1], L[ind + 2]) :
        f=1
        print(a, a, L[ind - 1], L[ind + 2])
    if f == 0:
        print(-1)
