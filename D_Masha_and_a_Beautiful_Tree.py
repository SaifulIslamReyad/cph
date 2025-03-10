# for _ in range(int(input())):
#     n = int(input())
#     L = list(map(int, input().split()))
#     step = 1
#     op = 0
#     while step < n:
#         for i in range(0, n, step * 2):
#             if L[i] > L[i + step]:
#                 L[i : i + step], L[i + step : i + step + step] = (
#                     L[i + step : i + step + step],
#                     L[i : i + step],
#                 )
#                 op += 1
#         step *= 2
#     print(op if L == list(range(1, n + 1)) else -1)





def recursive_sort(L, step, n, op):
    if step == n:
        return op if L == list(range(1, n + 1)) else -1

    for i in range(0, n, step * 2):
        if i + step < n and L[i] > L[i + step]:
            L[i : i + step], L[i + step : i + step + step] = (
                L[i + step : i + step + step],
                L[i : i + step],
            )
            op += 1

    return recursive_sort(L, step * 2, n, op)


for _ in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    print(recursive_sort(L, 1, n, 0))
