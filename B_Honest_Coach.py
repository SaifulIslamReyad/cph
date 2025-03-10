# https://codeforces.com/problemset/problem/1360/B
def quick_sort(L):
    if len(L) <= 1:return L
    pivot = L[len(L) // 2]
    left = [x for x in L if x < pivot]
    middle = [x for x in L if x == pivot]
    right = [x for x in L if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)



for _ in range(int(input())):
    n=int(input())
    L=(list(map(int, input().split())))
    L= quick_sort(L)
    ans = 10001
    for i in range(1,n):
        if L[i]-L[i-1]<ans : ans= L[i]-L[i-1]
    print(ans)
