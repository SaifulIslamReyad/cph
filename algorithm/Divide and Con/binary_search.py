import bisect

# lowerbound= bisect_left = smallest number which is greater than or equal to the target
# upperbound= bisect_right = smallest number which is greater than the target


def binary_bisect_left_efficient(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# print(binary_bisect_left_efficient([1, 3, 4, 7, 9], 5))


def binary_bisect_right_efficient(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# print(binary_bisect_right_efficient([1, 3, 4, 5, 5, 5, 7, 9], 5))


def binary_bisect_left(nums, target):
    h = len(nums) - 1
    l = 0
    if target > nums[h]:
        return h + 1
    elif target < nums[0]:
        return l
    while l <= h:
        mid = l + (h - l) // 2
        if nums[mid] == target:
            return mid
        elif (
            (mid == len(nums) - 1 and target > nums[mid - 1])
            or (mid == 0 and target < nums[mid + 1])
            or (target > nums[mid - 1] and target < nums[mid + 1])
        ):
            if target > nums[mid]:
                return mid + 1
            else:
                return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            h = mid - 1
    return -1


# print(binary_bisect_left([1, 3, 4, 7, 9], 5))


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Target not found

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search_recursive(
            arr, target, mid + 1, right
        )  # Search in the right half
    else:
        return binary_search_recursive(
            arr, target, left, mid - 1
        )  # Search in the left half


def binary_search(arr, target, left, right):
    if left > right:
        return -1  # Target not found

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)  # Search in the right half
    else:
        return binary_search(arr, target, left, mid - 1)  # Search in the left half


def floor_ceil(arr, target):
    left = 0
    right = len(arr) - 1
    floor = -1
    ceil = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid, mid
        elif arr[mid] < target:
            floor = mid
            left = mid + 1
        else:
            ceil = mid
            right = mid - 1
    return floor, ceil


# print(floor_ceil([1, 3, 4, 7, 9], 0))


def find_first_and_last_occurence(arr, target):
    left = 0
    right = len(arr) - 1
    first = -1
    last = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first, last


def find_first_last_occurrence_using_bisect(arr, target):
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target) - 1
    # Check if the target exists in the array
    if left < len(arr) and arr[left] == target:
        return left, right
    else:
        return -1, -1


def sqrt(x):
    if x < 2:
        return x
    left = 2
    right = x // 2
    while left <= right:
        mid = left + (right - left) // 2
        num = mid * mid
        if num == x:
            return mid
        elif num < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# print(sqrt(25))


def sqrt(x):
    if x < 2:
        return x
    left = 2
    right = x // 2
    ans = -1
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


print(sqrt(14))


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
