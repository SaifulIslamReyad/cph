def sqrt(x):
    if x < 2:
        return x
    left = 2
    right = x // 2
    ans=-1
    while left <= right:
        mid = left + (right - left) // 2
        num = mid * mid
        if num == x:
            return mid
        elif num < x:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans
print(sqrt(4))