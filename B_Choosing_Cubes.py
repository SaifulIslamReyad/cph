# https://codeforces.com/contest/1980/problem/B

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

for _ in range(int(input())):
    n,f,k = map(int, input().split())
    L=(list(map(int, input().split())))
    LL= merge_sort(L)[::-1]
    c= L.count(L[f-1])
    s= LL[:k].count(L[f-1])
    if c==s : print("YES")
    elif s==0 : print('NO') 
    else : print("MAYBE")

