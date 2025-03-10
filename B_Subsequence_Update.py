# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return merge_sort(left) + middle + merge_sort(right)
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
    n, l, r = map(int, input().split())
    l -= 1
    L = [*map(int, input().split())]
    b = L[:l] + merge_sort(L[l:])
    c = merge_sort(L[:r])[::-1] + L[r:]
    print(min(sum(b[l:r]), sum(c[l:r])))
