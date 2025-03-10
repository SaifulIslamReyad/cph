def quick_sort(L):
    if len(L) <= 1:return L
    pivot = L[len(L) // 2]
    left = [x for x in L if x < pivot]
    middle = [x for x in L if x == pivot]
    right = [x for x in L if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


L = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(L)
print(sorted_arr)
