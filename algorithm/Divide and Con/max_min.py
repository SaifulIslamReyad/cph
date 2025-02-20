def find_min_max(L, l, r):
    if l == r:    return L[l], L[l]
    if l == r-1:   return min(L[l], L[r]), max(L[l], L[r])
    mid = (l + r) // 2
    left_min, left_max = find_min_max(L, l, mid)
    r_min, r_max = find_min_max(L, mid + 1, r)
    return min(left_min, r_min), max(left_max, r_max)



L = [3, 1, 7, 8, 2, 6, 4]
min_val, max_val = find_min_max(L, 0, len(L) - 1)
print(f"Minimum: {min_val}, Maximum: {max_val}")
